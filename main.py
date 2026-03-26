from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("portfolio.html", {"request": request})

@app.get("/new")
def new_page(request: Request):
    return templates.TemplateResponse("new.html", {"request": request})