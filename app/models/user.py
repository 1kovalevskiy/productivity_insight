from datetime import date

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Column, String, Date

from app.core.db import Base


class User(SQLAlchemyBaseUserTable[int], Base):
    nickname = Column(String, nullable=False)
    create = Column(Date, default=date.today, nullable=False)
    update = Column(Date, default=date.today, nullable=False)
