from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import setting

# PostgreSQL connection URL format:
# postgresql+psycopg2://<username>:<password>@<host>:<port>/<database>

SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://{setting.DATABASE_USER_NAME}:{setting.DATABASE_PASSWORD}@{setting.DATABASE_HOST}:{setting.DATABASE_PORT}/{setting.DATABASE_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()



#--------------------------------------------------------------------------------------------
##  Connect with sqlite ##
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base


# SQLALCHAMY_DATABASE_URL = 'sqlite:///./datastorage.db'
# engine = create_engine(SQLALCHAMY_DATABASE_URL, connect_args={"check_same_thread": False})
# SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Base = declarative_base()

