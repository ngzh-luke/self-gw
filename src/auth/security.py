""" Authentication security operations """
# Adapted from https://github.com/zhanymkanov/fastapi_production_template/blob/main/src/auth/security.py

import bcrypt
# from datetime import datetime, timedelta
# from zoneinfo import ZoneInfo
from jwcrypto import jwt, jwk
from src.config import AUDIENCE, ISSUER
from utils import getALG


def hashPassword(password: str) -> bytes:
    pw = bytes(password, "utf-8")
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(pw, salt)


def checkPassword(password: str, password_in_db: bytes) -> bool:
    password_bytes = bytes(password, "utf-8")
    return bcrypt.checkpw(password_bytes, password_in_db)


def createAccessToken(data: dict, validWithinMins: int | None = None):
    toBeEncoded = data.copy()  # copy data for avoid making changes to original one
    if validWithinMins:
        expire = validWithinMins
        # datetime.now(tzinfo=ZoneInfo("UTC")) + \
        # timedelta(minutes=validWithinMins)
    else:
        expire = 15
        # datetime.now(tz=ZoneInfo("UTC")) + \
        # timedelta(minutes=15)

    # toBeEncoded.update({
    #     "exp": expire
    # })
    # al = 'HS256'
    al = getALG()
    key = jwk.JWK(generate='oct', size=512)
    # key.export()
    Token = jwt.JWT(header={"alg": al},
                    claims={"data": toBeEncoded, 'exp': expire, 'iss': ISSUER, 'aud': AUDIENCE})
    Token.make_signed_token(key)
    return str(Token)
