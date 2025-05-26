from sqlalchemy.orm import Session
import models



# Create new blog send data via request body
def create_blog(request: any, db: any):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

    return new_blog


# Get all data using query paramerers
def all_blogs(db):
    print('hello sir',)
    blogs = db.query(models.Blog).all()
    return blogs
