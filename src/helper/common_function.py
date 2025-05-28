from pydantic import BaseModel, Field, field_validator
import re

class HelperFunctions:
    def validate_email(cls, value):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", value):
            raise ValueError('Invalid email format')
        return value
    

commonFunction = HelperFunctions()