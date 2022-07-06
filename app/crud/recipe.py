from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import Recipe


class CRUDRecipe(CRUDBase):

    async def get_list(
            self,
            session : AsyncSession
    ):
        db_objs = await session.execute(
            select(self.model).where(self.model.status == 1)
        )
        return db_objs.scalars().all()


recipe_crud = CRUDRecipe(Recipe)
