from sqlalchemy import Integer, Column, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Character(Base):

    __tablename__ = "characters"
    id = Column(Integer, primary_key=True)
    character_name = Column(Text)
    side = Column(Text)
    talent = Column(Text)

    def __repr__(self):
        return f"Character(id={self.id}, name={self.name}, side={self.side}, talent={self.talent})"
