from sqlalchemy.orm import Session
from models import Blog
from fastapi import HTTPException, status
from sqlalchemy import desc, or_



# Create new blog send data via request body
def createBlog(request: any, db: any):
    new_blog = Blog(title=request.title, body=request.body)
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
        blogs = db.query(Blog).filter(Blog.is_deleted == False).order_by(Blog.id).offset(skip).limit(limit).all()
        
    else:
        blogs = (
            db.query(Blog)
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
    data = [
        {
            "s_no": index + 1,  # Serial number based on page & limit
            "id": item.id,
            "title": item.title,
            "body": item.body
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

