from fastapi import APIRouter
from .crud import *

router = APIRouter()

@router.get("/")
def get_home():
    return home()
