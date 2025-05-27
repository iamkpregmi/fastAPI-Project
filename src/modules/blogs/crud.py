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
    total_blogs = db.query(models.Blog).filter(models.Blog.is_deleted == False).count()
    if search_text == '':
        blogs = (
            db.query(models.Blog)
            .filter(models.Blog.is_deleted == False)
            .order_by(models.Blog.id)
            .offset(skip)
            .limit(limit)
            .all()
        )
    else:
        blogs = (
            db.query(models.Blog)
            .filter(
                models.Blog.is_deleted == False,
                or_(
                    models.Blog.title.ilike(f"%{search_text}%"),
                    models.Blog.body.ilike(f"%{search_text}%")
                )
            )
            .order_by(models.Blog.id)
            .offset(skip)
            .limit(limit)
            .all()
        )
    search_count = len(blogs)
    context = {
        "total_blogs": total_blogs,
        "search_count": search_count,
        "page": page,
        "limit": limit,
        "data": blogs
    }

    return context


#get single blog
def singleBlog(id,db):
    blog = db.query(models.Blog).filter((models.Blog.id == id) & (models.Blog.is_deleted == False)).first()
    
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with the id {id} is not available.')
    return blog


# Update blog
def updateBlog(id, request, db):
    blog = db.query(models.Blog).filter((models.Blog.id == id) & (models.Blog.is_deleted == False))

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog id {id} not found.')
    
    blog.update(request.model_dump())
    db.commit()
    return {'data': f'{id} Blog updated successfully.'}


def deleteBlog(id, db):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog id {id} not found.')
    
    # db.delete(blog) #hard delete data
    # db.commit()
    blog.is_deleted = True #soft delete data
    db.commit()
    db.refresh(blog)  # Optional: Refresh the object with latest DB state
    return {'data': f'Blog id {id} deleted successfully.'}

