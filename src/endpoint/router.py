""" Endpoint router """

from fastapi import APIRouter, Request, Response
from fastapi.responses import HTMLResponse, PlainTextResponse, RedirectResponse
from utils import TEMPLATES as t

endpointRouter = APIRouter()


@endpointRouter.get('/{url}', response_description='Redirect to the given url')
async def redirectByL(url: str = 'lukecreated.com'):
    return RedirectResponse(url=f"http://{url}")


# @endpointRouter.get('/{key}', response_description='Redirect to the given url of the key')
# async def redirectByK(key: str = 'lukecreated.com'):
#     return RedirectResponse(url=f"")
