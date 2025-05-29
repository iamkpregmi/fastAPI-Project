from fastapi.templating import Jinja2Templates


templates = Jinja2Templates(directory="templates")

def home(request):
    return templates.TemplateResponse("index.html", {"request": request, "name": "Krishna"})


def blogCategory(category):
    return {'data': f'You have selected {category.value} Category.'}