from pydantic import BaseModel, Field, field_validator
import re

class HelperFunctions:
    # Email validation
    def validate_email(cls, value):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", value):
            raise ValueError('Invalid email format')
        return value
    

    #Password Validation
    def validate_password(cls, value: str) -> str:
        if len(value) < 10:
            raise ValueError("Password must be at least 10 characters long")
        
        if not re.search(r"[A-Z]", value):
            raise ValueError("Password must contain at least one uppercase letter")
        
        if not re.search(r"[a-z]", value):
            raise ValueError("Password must contain at least one lowercase letter")
        
        if not re.search(r"[0-9]", value):
            raise ValueError("Password must contain at least one digit")
        
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", value):
            raise ValueError("Password must contain at least one special character")
        
        return value


commonFunction = HelperFunctions()