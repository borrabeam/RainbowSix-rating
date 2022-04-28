from sqlalchemy import Integer, Column, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class UserRating(Base):

    __tablename__ = "rating"
    id = Column(Integer, primary_key=True)
    user_name = Column(Text)
    rating = Column(Integer)


    def __repr__(self):
        return f"UserRating(id={self.id}, user_name={self.user_name}, rating={self.rating})"
