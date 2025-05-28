from fastapi import FastAPI
from modules.blogs.route import router as blog_router
from modules.users.route import router as user_router
import config

app = FastAPI()

#CSCR ALLOW
config.CSRF_ALLOW(app)

# Register routes with prefixes
app.include_router(blog_router, prefix="/blog", tags=["Blog"])
app.include_router(user_router, prefix="/user", tags=["User"])
