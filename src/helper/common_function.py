from pydantic import BaseModel, Field, field_validator
import re
from faker import Faker
from sqlalchemy.orm import Session
import models
from database import engine


fake = Faker()
#Create Table into Database
models.Base.metadata.create_all(engine)

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



# Fake blogs insert function
def insert_fake_blogs(total: int, db: Session):
    blogs = []
    for _ in range(total):
        fake_title = fake.paragraph(nb_sentences=1)
        fake_body = fake.paragraph(nb_sentences=3)

        blog = models.Blog(title=fake_title, body=fake_body, is_deleted=False, user_id="1")
        blogs.append(blog)

    db.bulk_save_objects(blogs)
    db.commit()
    print(f"{total} fake blogs inserted successfully.")

