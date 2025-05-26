from urllib import request
from fastapi import APIRouter, Depends
from .crud import *
from . import schema
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from typing import List

router = APIRouter()

#Create Table into Database
models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post('/create-blog', status_code = status.HTTP_201_CREATED)
def get_create_blog(request: schema.Blog, db : Session = Depends(get_db)):
    return create_blog(request, db)


@router.get('/blogs', status_code=status.HTTP_202_ACCEPTED)
def get_all_blogs(db : Session = Depends(get_db)):
    return all_blogs(db)


@router.get('/blog/{id}', status_code=status.HTTP_202_ACCEPTED)
def get_blog(id:int, db : Session = Depends(get_db)):
    return blog(id, db)


@router.put('/update/{id}', status_code=status.HTTP_202_ACCEPTED)
def get_update(id:int,request: schema.Blog, db : Session = Depends(get_db)):
    return updateBlog(id, request, db)


@router.delete('/delete/{id}', status_code=status.HTTP_200_OK)
def get_deleteBlog(id:int, db : Session = Depends(get_db)):
    return deleteBlog(id, db)