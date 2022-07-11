from datetime import date

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Column, String, Date, Boolean
from sqlalchemy.orm import relationship

from app.core.db import Base


class User(SQLAlchemyBaseUserTable[int], Base):
    nickname = Column(String, nullable=False)
    create = Column(Date, default=date.today, nullable=False)
    update = Column(Date, default=date.today, nullable=False)
    favorite = relationship("Recipe", secondary="favorite", back_populates='in_favorite')
    like = relationship("Recipe", secondary="like", back_populates='in_like')
    recipes = relationship("Recipe")
    # status = Column(Boolean, default=True, nullable=False)

