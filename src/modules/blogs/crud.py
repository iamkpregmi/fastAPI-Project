from sqlalchemy.orm import Session
import models
from fastapi import HTTPException, status
from sqlalchemy import desc, or_



# Create new blog send data via request body
def createBlog(request: any, db: any):
    new_blog = models.Blog(title=request.title, body=request.body)
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
    if search_text == 'string' or search_text == '':
        blogs = db.query(models.Blog).order_by(models.Blog.id).offset(skip).limit(limit).all()
    else:
        blogs = db.query(models.Blog).filter(or_(models.Blog.title.ilike(f"%{search_text}%"), models.Blog.body.ilike(f"%{search_text}%"))).order_by(models.Blog.id).offset(skip).limit(limit).all()
    total_blogs = db.query(models.Blog).count()
    context = {
        "total_blogs": total_blogs,
        "page": page,
        "limit": limit,
        "data": blogs
    }

    return context


#get single blog
def blog(id,db):
    blog = db.query(models.Blog).filter(models.Blog.id==id).first()
    
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with the id {id} is not available.')
    return blog


# Update blog
def updateBlog(id, request, db):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog id {id} not found.')
    
    blog.update(request.model_dump())
    db.commit()
    return {'data': f'{id} Blog updated successfully.'}


def deleteBlog(id, db):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog id {id} not found.')
    
    db.delete(blog)
    db.commit()
    return {'data': f'Blog id {id} deleted successfully.'}

