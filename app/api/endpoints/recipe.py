from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.user import current_user
from app.crud.recipe import recipe_crud
from app.models import User
from app.schemas.recipe import RecipeDB, RecipeCreate, RecipeListDB

router = APIRouter()


@router.post(
    '/',
    response_model_exclude_none=True,
    response_model=RecipeDB
)
async def create_recipe(
        recipe: RecipeCreate,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user),
):
    recipe = await recipe_crud.create(
        obj_in=recipe, session=session, user=user
    )
    return recipe


@router.get(
    '/{id}',
    response_model_exclude_none=True,
    response_model=RecipeDB
)
async def get_recipe(
        id: int,
        session: AsyncSession = Depends(get_async_session),
):
    recipe = await recipe_crud.get(
        obj_id=id, session=session
    )
    return recipe


@router.get(
    '/',
    response_model_exclude_none=True,
    response_model=list[RecipeListDB]
)
async def get_recipe(
        session: AsyncSession = Depends(get_async_session),
):
    recipes = await recipe_crud.get_list(session=session)
    return recipes
