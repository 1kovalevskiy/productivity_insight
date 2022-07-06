from datetime import date

from sqlalchemy import Column, ForeignKey, Date, Text, Boolean, Integer
from sqlalchemy.orm import relationship

from app.core.db import Base


class Like(Base):
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    recipe_id = Column(Integer, ForeignKey('recipe.id'), primary_key=True)


class Favorite(Base):
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    recipe_id = Column(Integer, ForeignKey('recipe.id'), primary_key=True)


class Recipe(Base):
    user_id = Column(Integer, ForeignKey('user.id'))
    create = Column(Date, default=date.today, nullable=False)
    update = Column(Date, default=date.today, nullable=False)
    name = Column(Text, nullable=False)
    type = Column(Text, nullable=False)
    description = Column(Text, nullable=False)
    steps = Column(Text, nullable=False)
    photo = Column(Text, nullable=False)
    status = Column(Boolean, default=1)
    in_favorite = relationship("User", secondary="favorite", back_populates='favorite')
    in_like = relationship("User", secondary="like", back_populates='like')
