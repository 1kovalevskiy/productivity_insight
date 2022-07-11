from fastapi import Depends, APIRouter
from fastapi_pagination import Page, Params, paginate
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.user import current_user, banned_user, current_superuser
from app.crud.admin import admin_crud
from app.crud.user import user_crud
from app.models import User
from app.schemas.user import UserDB, UserRead

router = APIRouter()


@router.patch(
    '/{id}/lock',
    response_model_exclude_none=True,
    dependencies=[Depends(current_superuser)]
)
async def lock_profile(
        id: int,
        session: AsyncSession = Depends(get_async_session),
):
    profile = await admin_crud.lock_user(
        id=id, session=session
    )
    return profile


@router.patch(
    '/{id}/unlock',
    response_model_exclude_none=True,
    dependencies=[Depends(current_superuser)]
)
async def unlock_profile(
        id: int,
        session: AsyncSession = Depends(get_async_session),
):
    profile = await admin_crud.unlock_user(
        id=id, session=session
    )
    return profile


@router.get(
    '/',
    response_model_exclude_none=True,
    dependencies=[Depends(current_superuser)],
    response_model=Page[UserRead | None]

)
async def get_profiles(
        params: Params = Depends(),
        session: AsyncSession = Depends(get_async_session),
):
    profiles = await admin_crud.get_multi(
        session=session
    )
    return paginate(profiles, params)
