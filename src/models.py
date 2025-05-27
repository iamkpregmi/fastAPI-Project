from database import Base
from sqlalchemy import Column, Integer, String, Boolean


class Blog(Base):
    __tablename__ = 'blogs'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String)
    body = Column(String)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    is_admin = Column(Boolean)
