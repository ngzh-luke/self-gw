""" Admin router """

from fastapi import APIRouter

adminRouter = APIRouter()


@adminRouter.get('/')
async def root():
    return {"message": "Hello World"}
