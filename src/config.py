import os
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

# Load from .env file
load_dotenv()

def CSRF_ALLOW(app):
    return app.add_middleware(
        CORSMiddleware,
        allow_origins=[f"{os.getenv('ALLOW_ORIGIN')}:{os.getenv('ALLOW_PORT')}"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

class Setting:
    DATABASE_HOST: str = os.getenv('HOST', '').strip()
    DATABASE_PORT: str = os.getenv('PORT', '').strip()
    DATABASE_USER_NAME: str = os.getenv('USER_NAME', '').strip()
    DATABASE_PASSWORD: str = os.getenv('PASSWORD', '').strip()
    DATABASE_NAME: str = os.getenv('DATABASE_NAME', '').strip()

setting = Setting()
