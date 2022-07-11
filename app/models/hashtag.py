# from sqlalchemy import Column, Text
# from sqlalchemy.orm import relationship
#
# from app.core.db import Base
#
#
# class Hashtag(Base):
#     name = Column(Text, nullable=False)
#     recipe = relationship("Recipe", secondary="recipeshashtag", back_populates='hashtag')
#
