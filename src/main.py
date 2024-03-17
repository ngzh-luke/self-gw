""" Starting point of the application """

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from typing import Any
import config
from root.router import router
from auth.router import authRouter
from admin.router import adminRouter
from endpoint.router import endpointRouter

app = FastAPI()
app.debug = bool(config.envDict['DEBUG'])
app.title = config.TITLE
app.version = config.VERSION
app.description = config.DESCRIPTION

app.include_router(router, tags=["Root"])
app.include_router(authRouter, prefix="/auth", tags=["Authentication"])
app.include_router(adminRouter, prefix='/gw-admin', tags=['Admin'])
app.include_router(endpointRouter, prefix='/r', tags=['Endpoint'])
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.exception_handler(StarletteHTTPException)
async def httpErrorHandler(request, exc: Any):
    return config.TEMPLATES.TemplateResponse(request=request, name="httpError.html", context={"code": str(exc.status_code), 'detail': exc.detail})
