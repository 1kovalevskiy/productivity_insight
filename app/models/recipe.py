from datetime import date

from sqlalchemy import Column, ForeignKey, Date, Text, Boolean, Integer

from app.core.db import Base


class Recipe (Base):
    user_id = Column(Integer, ForeignKey('user.id'))
    create = Column(Date, default=date.today, nullable=False)
    update = Column(Date, default=date.today, nullable=False)
    name = Column(Text, nullable=False)
    type = Column(Text, nullable=False)
    description = Column(Text, nullable=False)
    steps = Column(Text, nullable=False)
    photo = Column(Text, nullable=False)
    status = Column(Boolean, default=1)
