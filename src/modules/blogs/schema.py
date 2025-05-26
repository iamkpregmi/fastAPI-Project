from pydantic import BaseModel

class Blog(BaseModel):
    title: str
    body: str
    # is_published: Optional[bool] = False

