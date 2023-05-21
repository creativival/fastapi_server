from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi.staticfiles import StaticFiles
from fastapi import APIRouter

# router = APIRouter()
app = FastAPI()
# app.include_router(router)
templates = Jinja2Templates(directory='templates')

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get('/', response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse(
        'index.html',
        {
            'request': request
        }
    )


@app.get('/maps/{map_id}', response_class=HTMLResponse)
def get_map(map_id: str, request: Request):
    return templates.TemplateResponse(
        'map.html',
        {
            'request': request,
            'map_id': map_id
        }
    )