from database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship


class Blog(Base):
    __tablename__ = 'blogs'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String)
    body = Column(String)
    is_deleted = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('users.id'))

    creator = relationship('User', back_populates='blogs')


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    is_admin = Column(Boolean)

    blogs = relationship('Blog', back_populates='creator')
