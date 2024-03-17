""" Root router """

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, PlainTextResponse
from config import TEMPLATES as t
from config import VERSION, DESCRIPTION

router = APIRouter()


@router.get('/', response_class=HTMLResponse, response_description='Home page')
async def index(request: Request):
    return t.TemplateResponse(
        request=request, name="index.html")


@router.get('/...', response_description='GW version')
async def info():
    return PlainTextResponse(content=f"version: {VERSION}")
