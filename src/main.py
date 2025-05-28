from fastapi import FastAPI
from modules.blogs.route import router as blog_router
from modules.users.route import router as user_router
from modules.authentication.route import router as user_auhentication
import config

app = FastAPI(docs_url="/docs")

#CSCR ALLOW
config.CSRF_ALLOW(app)

# Register routes with prefixes
app.include_router(blog_router, prefix="/blog", tags=["Blog"])
app.include_router(user_router, prefix="/user", tags=["User"])
app.include_router(user_auhentication, tags=["Authentication"])

