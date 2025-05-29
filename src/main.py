from fastapi import FastAPI, Request
from modules.blogs.route import router as blog_router
from modules.users.route import router as user_router
from modules.authentication.route import router as user_authentication
import config
from fastapi.templating import Jinja2Templates

app = FastAPI(docs_url="/docs")

templates = Jinja2Templates(directory="templates")

# CSRF ALLOW 
config.CSRF_ALLOW(app)

# Register routes with prefixes
app.include_router(blog_router, prefix="/blog", tags=["Blog"])
app.include_router(user_router, prefix="/user", tags=["User"])
app.include_router(user_authentication, tags=["Authentication"])


@app.get('/')
def home_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "name": "Krishna"})
