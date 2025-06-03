from .crud import *
from fastapi import APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from . import schema


router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post('/login')
def user_login(request: schema.Login, db: Session = Depends(get_db)):
# def user_login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    return login(request, db)


@router.post('/logout')
def user_logout():
    return logout()


@router.post('/health-check', summary="Health Check", description="Health Check of API endpoint")
def api_health_check():
    return health_check()

