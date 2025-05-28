from pydantic import BaseModel, Field

class Blog(BaseModel):
    title: str
    body: str
    


class SearchBlog(BaseModel):
    search_text: str = Field(default="")
    page: int = Field(gt=0, default=1)
    limit: int = Field(gt=0, default=10)


class ShowBlogs(Blog):
    id: int


class User(BaseModel):
    name: str
    email: str
    password: str