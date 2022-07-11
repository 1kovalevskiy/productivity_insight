from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.user import current_user, banned_user
from app.crud.user import user_crud
from app.models import User
from app.schemas.user import UserDB

router = APIRouter()


@router.get(
    '/me',
    response_model_exclude_none=True,
    response_model=UserDB
)
async def get_my_profile(
        user: User = Depends(banned_user),
        session: AsyncSession = Depends(get_async_session),
):
    profile = await user_crud.get_profile_db(
        obj_id=user.id, session=session
    )
    return profile


@router.get(
    '/top',
    response_model_exclude_none=True,
    response_model=list[UserDB],
    dependencies=[Depends(current_user)]
)
async def get_top_users(
        session: AsyncSession = Depends(get_async_session),
):
    profiles = await user_crud.get_top(
        session=session
    )
    return profiles
