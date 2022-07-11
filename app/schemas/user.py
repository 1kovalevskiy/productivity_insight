from datetime import date

from fastapi_users import schemas
from pydantic import BaseModel


class UserRead(schemas.BaseUser[int]):
    nickname: str
    create: date
    update: date


class UserCreate(schemas.BaseUserCreate):
    nickname: str


class UserUpdate(schemas.BaseUserUpdate):
    nickname: str
    update: date
    is_active: bool


class UserDB(BaseModel):
    id: int
    email: str
    nickname: str
    is_active: bool
    count: int

    class Config:
        orm_mode = True
