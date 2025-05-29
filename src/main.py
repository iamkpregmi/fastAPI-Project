from fastapi import FastAPI
from modules.blogs.route import router as blog_router
from modules.users.route import router as user_router
from modules.testing.route import router as testing_router
from modules.authentication.route import router as user_authentication
import config

app = FastAPI(docs_url="/docs")



# CSRF ALLOW 
config.CSRF_ALLOW(app)

# Register routes with prefixes
app.include_router(blog_router, prefix="/blog", tags=["Blog"])
app.include_router(user_router, prefix="/user", tags=["User"])
app.include_router(user_authentication, tags=["Authentication"])
app.include_router(testing_router, prefix="/testing", tags=["Testing"])

