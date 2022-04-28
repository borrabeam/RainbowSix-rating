from rainbow import RainbowSix

rainbowsix_db = RainbowSix.get_instance()

character_dao = rainbowsix_db.get_character_dao()
rating_dao = rainbowsix_db.get_rating_dao()

print(character_dao.get_character())