import random


class Player:
    """
    ANVÄNDAREN
    """

    def __init__(self, player_avatar: list, player_name) -> None:

        # Player Status
        self.name: str = player_name
        self.player_lift: int = 3
        self.player_hp: int = 10
        self.player_damage: int = random.randint(5, 10)
        self.player_lvl: int = 1
        self.player_armor: str = random.choice(["Heavyarmor", "Lightarmor"])

        # Player Looks
        self.skin_color: str
        self.hair_color: str
        self.eye_color: str
        self.height: int
        self.width: int


def player_creater():
    """
    CREATING THE USER PLAYER

    Returns:
        _type_: _description_
    """

    base_blueprint_avatar = {
        "Skin color": str,
        "Hair color": str,
        "Body shape": str,
        "Eye color": str,
        "Height": int,
        "Weight": int
    }
