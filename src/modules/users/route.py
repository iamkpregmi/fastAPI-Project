from fastapi import APIRouter, status, Depends
from .crud import *
from . import schema
from database import SessionLocal, engine
from sqlalchemy.orm import Session
import models




router = APIRouter()

#Create Table into Database
models.Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register", status_code = status.HTTP_201_CREATED)
def register_User(request: schema.User, db : Session = Depends(get_db)):
    return registerUser(request, db)


@router.get('/get-user/{id}', response_model=schema.ShowUser)
def get_user(id:int, db : Session = Depends(get_db)):
    return getUser(id, db)

