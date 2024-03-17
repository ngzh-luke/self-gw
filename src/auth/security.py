""" Authentication security operations """
# Adapted from https://github.com/zhanymkanov/fastapi_production_template/blob/main/src/auth/security.py

import bcrypt


def hashPassword(password: str) -> bytes:
    pw = bytes(password, "utf-8")
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(pw, salt)


def checkPassword(password: str, password_in_db: bytes) -> bool:
    password_bytes = bytes(password, "utf-8")
    return bcrypt.checkpw(password_bytes, password_in_db)
