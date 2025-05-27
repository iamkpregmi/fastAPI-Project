from fastapi import APIRouter
from .crud import *
from . import schema

router = APIRouter()

@router.post("/register")
def register_User(request: schema.User):
    return registerUser(request)
