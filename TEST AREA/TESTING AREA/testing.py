import random
from tabulate import tabulate


class Player:
    """
    ANVÄNDAREN
    """

    def __init__(self, player_avatar: list[tuple[str, str]]) -> None:

        # Player Status
        self.name: str = player_avatar[0][1]
        self.player_lift: int = 3
        self.player_hp: int = 10
        self.player_damage: int = random.randint(5, 10)
        self.player_lvl: int = 1
        self.player_armor: str = random.choice(['Heavyarmor', 'Lightarmor'])

        # Player Looks
        self.skin_color: str = player_avatar[1][1]
        self.hair_color: str = player_avatar[2][1]
        self.body_shape: str = player_avatar[3][1]
        self.eye_color: str = player_avatar[4][1]
        self.height: str = player_avatar[5][1]
        self.weight: str = player_avatar[6][1]

    def print_player_stats(self):
        """
        Prints out a table of how the player looks
        """
        table_stats_data = [
            ["Player Stats", ""],
            ["Name", self.name],
            ["Life", self.player_lift],
            ["Level", self.player_lvl],
            ["Health", self.player_hp],
            ["Damage", self.player_damage],
            ["Armor", self.player_armor]
        ]
    # FUNCTION FOR PRINTING OUT THE PLAYER STATS
        print(tabulate(table_stats_data, headers="firstrow", tablefmt="psql"))

    def print_player_avatar(self):
        """
        Prints out a player avatar looks
        """

        table_stats_avatar = [
            ["Avatar", ""],
            ["Skin color", self.skin_color],
            ["Hair color", self.hair_color],
            ["Body shape", self.body_shape],
            ["Eye color", self.eye_color],
            ["Height", self.height],
            ["Weight", self.weight],
        ]
    # FUNCTION FOR PRINTING OUT THE PLAYER LOOKS
        print(tabulate(table_stats_avatar, headers="firstrow", tablefmt="psql"))


def player_creater():
    """
    CREATING THE USER PLAYER

    Returns:
        lsit: player looks
    """
    user_awnser: str = ''

    base_blueprint_avatar = {
        'User name': '',
        'Skin color': '',
        'Hair color': '',
        'Body shape': '',
        'Eye color': '',
        'Height': '0',
        'Weight': '0'
    }

    for (key, value) in list(base_blueprint_avatar.items()):
        print(key)
        print(value)
        user_awnser = input(
            f'What {key} does your character have [TYPE ONLY LETTHERS] ? ')

        if isinstance(value, str):
            #         while not user_awnser.isalpha():
            #             user_awnser = input(
            #                 f'What {key} does your character have [TYPE ONLY LETTHERS] ? ')
            #     else:
            #         while not user_awnser.isnumeric():
            #             user_awnser = input(
            #                 f'What {key} does your character have [TYPE ONLY NUMBERS] ? ')

        base_blueprint_avatar[key] = str(user_awnser)
    print(list(base_blueprint_avatar.items()))


if __name__ == '__main__':
    player_creater()
    input()
