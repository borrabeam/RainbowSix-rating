from sqlalchemy.orm import Session
from models.character_model import Character

class CharacterDao:

    def __init__(self, session:Session):
        self.__session = session

    def get_character(self):
        
        return self.__session.query(Character).all()
    
    def get_character_id(self,id):
        
        return self.__session.query(Character).filter_by(id=id).first()
    
    def add_character(self, character: Character):

        self.__session.add(character)
        self.__session.commit()
        print("Added success.")
    
    def delete_character(self,id):
        
        find_character = self.__session.query(Character).filter_by(id=id).first()
        self.__session.delete(find_character)
        self.__session.commit()
        print("Delete success.")

    def update_character(self,id, update_character_name):
        
        find_character = self.__session.query(Character).filter_by(id=id).first()
        find_character.character_name = update_character_name
        self.__session.commit()
        print("Updated character name success.")