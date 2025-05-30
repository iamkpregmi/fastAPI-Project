from pydantic import BaseModel, Field, field_validator
from typing import Optional, List
from helper.common_function import commonFunction
import re


class User(BaseModel):
    name: str = Field(default="test",max_length=50)
    email: str = Field(default="test@test.com")
    password: str = Field(default="")
    is_admin: Optional[bool] = False

    #this code responsible for the email validation
    @field_validator('email')
    def validate_email(cls, value):
        return commonFunction.validate_email(value)
    
    #this code responsible for the password validation
    @field_validator('password')
    def validate_password(cls, value):
        return commonFunction.validate_password(value)


class ShowUser(BaseModel):
    name: str
    email: str
    is_admin: bool


class Blog(BaseModel):
    title: str
    body: str


class ShowUserBlog(BaseModel):
    name: str
    email: str

    blogs: List['Blog'] = []
