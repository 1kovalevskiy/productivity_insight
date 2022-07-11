from datetime import date

from pydantic import BaseModel, HttpUrl, Field


class RecipeBase(BaseModel):
    name: str
    type: str
    description: str
    photo: HttpUrl = Field()


class RecipeCreate(RecipeBase):
    steps: str


class RecipeListDB(RecipeBase):
    id: int
    user_id: int
    create: date
    update: date
    status: bool

    class Config:
        orm_mode = True


class RecipeDB(RecipeListDB):
    steps: str
