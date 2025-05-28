import models
from fastapi import status, HTTPException
from helper.hashing import Hashing
from helper import JWTtoken


def login(request, db):
    user = db.query(models.User).filter(models.User.email == request.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials.")
    
    if not Hashing.verifyPassword(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Password.")
    
    #implement jwt token
    result =  JWTtoken.create_access_token(data={'sub':user.email})

    return result
