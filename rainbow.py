from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dao.character_dao import CharacterDao
from dao.rating_dao import UserRatingDao

class RainbowSix:
    
    character_dao = None
    rating_dao = None
    instance = None


    def __init__(self):
        engine = create_engine("sqlite:///rainbow_data.db")
        Session = sessionmaker(bind=engine)
        self.__db_session = Session()

    @staticmethod
    def get_instance():       
        if RainbowSix.instance is None:
            RainbowSix.instance = RainbowSix()
        return RainbowSix.instance

    def get_character_dao(self):
        
        if self.character_dao is None:
            self.character_dao = CharacterDao(session=self.__db_session)
        return self.character_dao
    
    def get_rating_dao(self):
        
        if self.rating_dao is None:
            self.rating_dao = UserRatingDao(session=self.__db_session)
        return self.rating_dao
    
    def close_db(self):
        
        self.__db_session.close()
