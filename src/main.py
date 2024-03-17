from fastapi import FastAPI
import config
from root.router import router
from auth.router import authRouter

app = FastAPI()
app.debug = bool(config.envDict['DEBUG'])
app.title = config.TITLE
app.version = config.VERSION
app.description = config.DESCRIPTION

app.include_router(router, tags=["Root"])
app.include_router(authRouter, prefix="/auth", tags=["Authentication"])
