from pydantic import BaseModel, Field, field_validator
from typing import Optional
import re

class User(BaseModel):
    name: str = Field(default="test",max_length=50)
    email: str = Field(default="test@test.com")
    password: str = Field(default="")
    is_admin: Optional[bool] = False

    #this code responsible for the email validation
    @field_validator('email')
    def validate_email(cls, value):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", value):
            raise ValueError('Invalid email format')
        return value


class ShowUser(BaseModel):
    name: str
    email: str
    is_admin: bool

