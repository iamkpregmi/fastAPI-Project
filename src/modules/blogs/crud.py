from sqlalchemy.orm import Session
import models
from fastapi import HTTPException, status



# Create new blog send data via request body
def create_blog(request: any, db: any):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

    return new_blog


# Get all data using query paramerers
def all_blogs(db):
    blogs = db.query(models.Blog).all()
    return blogs


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

