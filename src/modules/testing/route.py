from fastapi import APIRouter
from .crud import *
from fastapi import Request
from enums.common_enum import BlogCategory

router = APIRouter()

@router.get('/')
def home_page(request: Request):
    return home(request)


@router.get('/blog-category/{category}')
def blog_category(category: BlogCategory):
    return blogCategory(category)

