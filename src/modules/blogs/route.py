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


@router.post('/create-blog')
def get_create_blog(request: schema.Blog, db : Session = Depends(get_db)):
    create_blog(request, db)


@router.get('/blogs')
def get_all_blogs(db : Session = Depends(get_db)):
    all_blogs(db)