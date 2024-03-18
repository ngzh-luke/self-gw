""" Utilities functions for Authentication """

from schemas import User
from security import checkPassword
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jwcrypto import jwt, jwk
from config import credentials


def getUser(db, userID: str):
    if userID in db:
        userData = db[userID]
        return User(**userData)


def authenticateUser(db, userID: str, password: str):
    user = getUser(db=db, userID=userID)
    if not user:
        # if user did not exists
        return False
    if not checkPassword(password=password, password_in_db=user.password):
        # if password is not match
        return False
    return user


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/gen-token")


async def getCurrentUser(key: dict, token: str = Depends(oauth2_scheme), ):
    credException = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                  detail='Could not validate credentials', headers={"WWW-Authenticate": "Bearer"})
    try:
        k = jwk.JWK(**key)
        ET = jwt.JWT(key=k, jwt=token, expected_type="JWE")
        ST = jwt.JWT(key=k, jwt=ET.claims)
        claims = ST.claims
    except jwt.JWException:
        raise credException
    user = getUser(credentials, userID=claims.data.userID)
    if user == None:
        raise credException
    return user
