import models
from helper.hashing import Hashing
from fastapi import HTTPException, status


def registerUser(request, db):
    # new_user = models.User(**request.model_dump())
    encrypted_password = Hashing.hashPassword(request.password)
    new_user = models.User(
        name = request.name,
        email = request.email,
        password = encrypted_password,
        is_admin = request.is_admin
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def getUser(id,db):
    user_obj = db.query(models.User).filter(models.User.id == id).first()

    if not user_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User id {id} not found.')
    
    return user_obj
