from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


SQLALCHAMY_DATABASE_URL = 'sqlite:///./datastorage.db'
engine = create_engine(SQLALCHAMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()




#----------------------------------------------------------------------------------------------
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base

# # For mysql-connector-python:
# # SQLALCHEMY_DATABASE_URL = 'mysql+mysqlconnector://<username>:<password>@<host>/<database_name>'
# SQLALCHEMY_DATABASE_URL = 'mysql+mysqlconnector://root:1234@localhost:3306/blogdb'

# engine = create_engine(SQLALCHEMY_DATABASE_URL)
# SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Base = declarative_base()