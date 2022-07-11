from sqlalchemy import select, func, desc
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import User, Recipe


class CRUDUser(CRUDBase):

    async def get_profile_db(
            self,
            obj_id: int,
            session: AsyncSession,
    ):
        db_obj = await session.execute(
            select(
                self.model,
                func.count(Recipe.id).label('count')
            ).join(
                Recipe
            ).where(
                self.model.id == obj_id,
            )
        )
        db_data = db_obj.first()
        if db_data.User:
            result = db_data.User.__dict__
            result['count'] = db_data.count
        return result

    async def get_top(
            self,
            session: AsyncSession,
    ):
        sel = select(
            self.model, func.count(Recipe.id).label('count')
        ).join(
            Recipe
        ).where(
            self.model.id == Recipe.user_id
        ).limit(
            10
        ).group_by(
            self.model
        ).order_by(
            desc('count')
        )
        db_obj = await session.execute(sel)
        db_data = db_obj.all()
        result = []
        for data in db_data:
            elem = data.User.__dict__
            elem['count'] = data.count
            result.append(elem)
        return result


user_crud = CRUDUser(User)
