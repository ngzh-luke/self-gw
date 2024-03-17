from fastapi import APIRouter


authRouter = APIRouter()


@authRouter.get('/')
async def root():
    return {"message": "Hello World"}
