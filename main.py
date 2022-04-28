from rainbow import RainbowSix
from models.character_model import Character
from models.rating_model import UserRating

rainbowsix_db = RainbowSix.get_instance()

character_dao = rainbowsix_db.get_character_dao()
rating_dao = rainbowsix_db.get_rating_dao()

print(character_dao.get_character())

# new_character = Character(id=51, character_name="Beam",side="ATTACKER",talent="Fly")
# character_dao.add_character(new_character)
# print(character_dao.get_character_id("51"))