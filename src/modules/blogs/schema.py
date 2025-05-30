from pydantic import BaseModel, Field
from typing import List

class Blog(BaseModel):
    title: str
    body: str
    


class SearchBlog(BaseModel):
    search_text: str = Field(default="")
    page: int = Field(gt=0, default=1)
    limit: int = Field(gt=0, default=10)


class ShowUser(BaseModel):
    name: str
    email: str
    

class ShowBlogs(BaseModel): # this is for the get specific field
    id: int
    title: str
    body: str
    creator: ShowUser # Show user info


class User(BaseModel):
    name: str
    email: str
    password: str
