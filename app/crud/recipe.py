from sqlalchemy import select, func, desc
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import Recipe, Like


class CRUDRecipe(CRUDBase):

    async def get_list(
            self,
            session: AsyncSession,
            name: str = None,
            type_: str = None,
            author: int = None
    ):
        sel = select(
            self.model,
        ).where(
            self.model.status == 1
        ).order_by(
            self.model.create.desc()
        ).order_by(
            self.model.name.asc()
        )
        if name:
            sel = sel.where(self.model.name.contains(name))
        if type_:
            sel = sel.where(self.model.type_.contains(type_))
        if author:
            sel = sel.where(self.model.user_id == author)
        db_objs = await session.execute(sel)
        return db_objs.scalars().all()


recipe_crud = CRUDRecipe(Recipe)
