from datetime import date

from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    nickname: str
    create: date
    update: date


class UserCreate(schemas.BaseUserCreate):
    nickname: str


class UserUpdate(schemas.BaseUserUpdate):
    nickname: str
    update: date
