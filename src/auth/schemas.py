""" Schemas """
# Adapted from https://github.com/zhanymkanov/fastapi_production_template/blob/main/src/auth/schemas.py

import re as regx
from pydantic import Field, field_validator

from src.models import CustomModel

STRONG_PASSWORD_PATTERN = regx.compile(
    r"^(?=.*[\d])(?=.*[!@#$%^&*])[\w!@#$%^&*]{6,128}$")


class AuthUser(CustomModel):
    username: str = Field(min_length=3, max_length=25)
    password: str = Field(min_length=6, max_length=256)

    @field_validator("password", mode="after")
    @classmethod
    def valid_password(cls, password: str) -> str:
        if not regx.match(STRONG_PASSWORD_PATTERN, password):
            raise ValueError(
                "Password must contain at least "
                "one lower character, "
                "one upper character, "
                "digit or "
                "special symbol"
            )

        return password


class UserResponse(CustomModel):
    username: str
