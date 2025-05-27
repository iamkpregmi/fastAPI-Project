from urllib import request
from fastapi import APIRouter, Depends
from .crud import *
from . import schema
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from typing import List, Dict

router = APIRouter()

#Create Table into Database
models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create single blog data
@router.post('/create-blog', status_code = status.HTTP_201_CREATED)
def create_blog(request: schema.Blog, db : Session = Depends(get_db)):
    return createBlog(request, db)


# Get all blogs data
@router.post('/blogs', status_code=status.HTTP_202_ACCEPTED)
def all_blogs(request: schema.SearchBlog, db : Session = Depends(get_db)):
    return allBlogs(request, db)


# Get single blog data
@router.get('/blog/{id}', status_code=status.HTTP_202_ACCEPTED, response_model= schema.ShowBlogs)
def blog(id:int, db : Session = Depends(get_db)):
    return singleBlog(id, db)


# Update blog data
@router.put('/update/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_Blog(id:int,request: schema.Blog, db : Session = Depends(get_db)):
    return updateBlog(id, request, db)


# Delete single blog data
@router.delete('/delete/{id}', status_code=status.HTTP_200_OK)
def delete_Blog(id:int, db : Session = Depends(get_db)):
    return deleteBlog(id, db)

