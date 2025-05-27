from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from modules.blogs.route import router as blog_router
from modules.users.route import router as user_router

app = FastAPI()


# This is for the allow milleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # Angular dev server request
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes with prefixes
app.include_router(blog_router, prefix="/blog", tags=["Blog"])
app.include_router(user_router, prefix="/user", tags=["User"])
