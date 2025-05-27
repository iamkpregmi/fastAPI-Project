from pydantic import BaseModel, Field, field_validator
from typing import Optional
import re

class User(BaseModel):
    name: str = Field(default="default value",max_length=50)
    age: int = Field(gt=0)
    email: str
    password: str
    is_admin: Optional[bool] = False

    #this code responsible for the email validation
    @field_validator('email')
    def validate_email(cls, value):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", value):
            raise ValueError('Invalid email format')
        return value

