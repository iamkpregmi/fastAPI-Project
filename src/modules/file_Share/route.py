from .crud import *
from fastapi import APIRouter


router = APIRouter()


@router.get('/file-share')
def online_file_share():
    return home()

