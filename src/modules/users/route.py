from fastapi import APIRouter
from .crud import profile

router = APIRouter()

@router.get("/profile")
def get_profile():
    return profile()
