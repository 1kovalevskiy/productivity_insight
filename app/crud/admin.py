from sqlalchemy import select, func, desc
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import Recipe, Like, User


class CRUDAdmin(CRUDBase):

    async def lock_user(
            self,
            id: int,
            session: AsyncSession
    ):
        db_obj = await session.execute(
            select(self.model).where(
                self.model.id == id
            )
        )
        db_obj = db_obj.scalars().first()
        setattr(db_obj, 'is_active', False)
        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj

    async def unlock_user(
            self,
            id: int,
            session: AsyncSession
    ):
        db_obj = await session.execute(
            select(self.model).where(
                self.model.id == id
            )
        )
        db_obj = db_obj.scalars().first()
        setattr(db_obj, 'is_active', True)
        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj


admin_crud = CRUDAdmin(User)
