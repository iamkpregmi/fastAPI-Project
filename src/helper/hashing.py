from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hashing():
    def hashPassword(password):
        return pwd_context.hash(password)

    def verifyPassword(plain_password,hash_password):
        return pwd_context.verify(plain_password,hash_password)
