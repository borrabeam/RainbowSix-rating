from sqlalchemy.orm import Session
from models.rating_model import UserRating

class UserRatingDao:

    def __init__(self, session:Session):
        self.__session = session

    def get_rating(self):
        
        return self.__session.query(UserRating).all()
    
    def get_rating_id(self,id):
        
        return self.__session.query(UserRating).filter_by(id=id).first()
    
    def add_rating(self, rating: UserRating):

        self.__session.add(rating)
        self.__session.commit()
        print("Added success.")
    
    def delete_rating(self,id):
        
        find_user = self.__session.query(UserRating).filter_by(id=id).first()
        self.__session.delete(find_user)
        self.__session.commit()
        print("Delete success.")

    def update_rating(self,id, update_rating):
        
        find_rating = self.__session.query(UserRating).filter_by(id=id).first()
        find_rating.rating = update_rating
        self.__session.commit()
        print("Updated character name success.")
