""" Endpoint router """

from fastapi import APIRouter, Request, Response
from fastapi.responses import HTMLResponse, PlainTextResponse, RedirectResponse
from config import TEMPLATES as t

endpointRouter = APIRouter()


@endpointRouter.get('/{url}', response_description='Redirect to the given url')
async def endpoint(url: str = 'lukecreated.com'):
    return RedirectResponse(url=f"http://{url}")
