from sqlalchemy.orm import Session
from models import Blog
from fastapi import HTTPException, status
from sqlalchemy import desc, or_
from fastapi import UploadFile
from fastapi.responses import JSONResponse
import shutil
import os
import re
from sqlalchemy.orm import joinedload



# Create new blog send data via request body
def createBlog(request: any, db: any):
    new_blog = Blog(title=request.title, body=request.body, user_id='1')
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

    return new_blog


# Get all data using query paramerers
def allBlogs(request, db):
    search_text = request.search_text
    page = request.page
    limit = request.limit
    skip = (page - 1) * limit
    total_blogs = db.query(Blog).filter(Blog.is_deleted == False).count()

    if search_text == '':
        blogs = db.query(Blog).options(joinedload(Blog.creator)).filter(Blog.is_deleted == False).order_by(Blog.id).offset(skip).limit(limit).all()
        
    else:
        blogs = (
            db.query(Blog)
            .options(joinedload(Blog.creator))
            .filter(
                Blog.is_deleted == False,
                or_(
                    Blog.title.ilike(f"%{search_text}%"),
                    Blog.body.ilike(f"%{search_text}%")
                )
            )
            .order_by(Blog.id)
            .offset(skip)
            .limit(limit)
            .all()
        )
    search_result = len(blogs)
    #cor the get specific data
    # data=[{"id":item.id,
    #        "title":item.title,
    #        "body": item.body,
    # } for item in blogs]

    for i in blogs:
        print(i.__dict__)

    data = [
        {
            "s_no": index + 1,  # Serial number based on page & limit
            "id": item.id,
            "title": item.title,
            "body": item.body,
            "creator": {
                "name": item.creator.name,
                "email": item.creator.email
            }
        }
        for index, item in enumerate(blogs)
    ]

    context = {
        "total_blogs": total_blogs,
        "search_result": search_result,
        "page": page,
        "limit": limit,
        "data": data
    }

    return context


#get single blog
def singleBlog(id,db):
    blog = db.query(Blog).filter((Blog.id == id) & (Blog.is_deleted == False)).first()
    
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with the id {id} is not available.')
    return blog


# Update blog
def updateBlog(id, request, db):
    blog = db.query(Blog).filter((Blog.id == id) & (Blog.is_deleted == False))

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog id {id} not found.')
    
    blog.update(request.model_dump())
    db.commit()
    return {'data': f'{id} Blog updated successfully.'}


def deleteBlog(id, db): 
    blog = db.query(Blog).filter(Blog.id == id).first()

    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog id {id} not found.')
    
    # db.delete(blog) #hard delete data
    # db.commit()
    blog.is_deleted = True #soft delete data
    db.commit()
    db.refresh(blog)  # Optional: Refresh the object with latest DB state
    return {'data': f'Blog id {id} deleted successfully.'}



def upload_file(file: UploadFile):
    os.makedirs("assets", exist_ok=True)  # create directory if not exist
    file_location = f"assets/{file.filename}"
    allowed_types = ["image/png", "image/jpeg", "image/jpg"]
    filename = file.filename
    # for the check file type
    if file.content_type not in allowed_types:
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail="Invalid file type. Allowed types are: png, jpeg, jpg",
        )
    # for the check file name
    if not re.match(r"^[a-zA-Z0-9_\-.]+$", filename):
        raise HTTPException(
            status_code=400, detail="Invalid filename: only alphanumeric, underscores, hyphens, and dots are allowed."
        )

    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return JSONResponse(content={
        "filename": file.filename,
        "content_type": file.content_type,
        "message": "File uploaded successfully!"
    })
