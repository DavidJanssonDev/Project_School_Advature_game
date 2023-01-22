"""
    THIS IS THE FILE WHERE EVERY CLASS TAHT IS USED IN THE CODE ARE
"""

import random

from tabulate import tabulate

# ============================================================================
#                              PLAYER
# ============================================================================


class Player:
    """
    ANVÄNDAREN
    """

    def __init__(self, player_avatar: list[tuple[str, str]]) -> None:
        # Player Status
        self.p_turn = 0
        self.name: str = player_avatar[0][1].title()
        self.player_lvl: int = 0

        self.player_life: int = 3
        self.player_max_hp: int = 10
        self.player_hp: int = 10

        self.player_damage: int = random.randint(5, 10)
        self.player_armor: int = random.randint(1, 3)

        self.player_debuff: list[list] = []
        self.player_buff: list[list] = []
        self.player_inventory: dict = {
            'item 1': None,
            'item 2': None,
            'item 3': None,
            'item 4': None,
            'item 5': None,
        }

        self.player_potions: dict[str, int] = {
            'health': 3,
            'damage': 3,
            'armor': 3,
        }

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
            ["Life", self.player_life],
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

    def drink_potions(self, type_of_potion: str):
        """

        Adds a buff to the player when driking 

        Args:
            type_of_potion (str): what postion are the user drinking
            player (Player): _description_
        """
        effect: float = 0.0
        end_of_buff: int = self.p_turn + 2
        match type_of_potion:
            case 'damage':
                effect = 1.1
            case 'health':
                effect = 1.1
            case 'armor':
                effect = 1.07
        self.player_buff.append([type_of_potion, effect, end_of_buff])


# ============================================================================
#                               MONSTER
# ============================================================================


class Monster:
    """

    MONSTER FOR A PLAYER, EMENY THAT PLAYER WILL FIGHT IN THE GAME

    """

    def __init__(self, moster_level: int) -> None:
        self.moster_level = moster_level
        self.name: str = ""
        self.health: int = 0
        self.damage: int = 0
        self.armor: int = 0
        self.missing_luck: float = 0.0

    def stat_change(self) -> None:
        """

        Generate the stats for the monster
1-10
1-15
10-20

        """
        match self.moster_level:
            case 1:
                self.name: str = "Bob"
                self.health: int = 10
                self.damage: int = random.randint(1, 10)
                self.armor: int = 0
            case 2:
                self.name: str = "Bob 2.0"
                self.health: int = 20
                self.damage: int = random.randint(1, 15)
                self.armor: int = random.randint(1, 3)
            case 3:
                self.name: str = "Bob 3.0"
                self.health: int = 30
                self.damage: int = random.randint(1, 20)
                self.armor: int = random.randint(1, 4)
            case 4:
                self.name: str = "Bob 4.0"
                self.health: int = 40
                self.damage: int = random.randint(1, 30)
                self.armor: int = random.randint(1, 5)
            case 5:
                self.name: str = "Bob 5.0"
                self.health: int = 50
                self.damage: int = random.randint(1, 40)
                self.armor: int = random.randint(1, 5)
            case 6:
                self.name: str = "Bob 7.0"
                self.health: int = 60
                self.damage: int = random.randint(1, 50)
                self.armor: int = random.randint(1, 5)
            case 7:
                self.name: str = "Bob 8.0"
                self.health: int = 70
                self.damage: int = random.randint(1, 60)
                self.armor: int = random.randint(1, 6)
            case 8:
                self.name: str = "Bob 9.0"
                self.health: int = 80
                self.damage: int = random.randint(1, 70)
                self.armor: int = random.randint(1, 7)

            case 9:
                self.name: str = "Bob 10.0"
                self.health: int = 90
                self.damage: int = random.randint(1, 80)
                self.armor: int = random.randint(1, 8)

            case 10:
                self.name: str = "FINAL BOB"
                self.health: int = 1000
                self.damage: int = random.randint(1, 90)
                self.armor: int = random.randint(1, 9)


# ============================================================================
#                               MONSTER
# ============================================================================

def luck_calculation() -> list[float]:
    """
    HOW MUCH LUCK THE GAME HAVE
    """
    damage_boost_luck: float = 0
    armor_boost_luck: float = 0

    max_health_boost_luck: float = 0

    damage_boost_luck = random.random()
    armor_boost_luck = random.random()

    max_health_boost_luck = random.random()

    summa = sum([damage_boost_luck, armor_boost_luck, max_health_boost_luck])

    damage_boost_luck = damage_boost_luck / summa
    armor_boost_luck = armor_boost_luck / summa

    max_health_boost_luck = max_health_boost_luck / summa

    stats_boost_porcentage = [
        damage_boost_luck, armor_boost_luck, max_health_boost_luck]
    return stats_boost_porcentage


class Item:
    """
    item
    """

    def __init__(self, rarity: str, item_name: str) -> None:
        self.rarity = rarity
        self.item_name = item_name

        self.damage_boost: int = 0
        self.max_hp_boost: int = 0
        self.armor_boost: int = 0

    def __str__(self) -> str:
        return f"""

    This artefact is called {self.item_name} and has rarity of {self.rarity}

    Effected:

        Damage Multiplier : {self.damage_boost}
        Max Health Boost  : {self.max_hp_boost} %
        Armor Boost       : {self.armor_boost} %
    """

    def genatate_stat(self):
        """
        somthing
        """
        number_of_stats: int = 0
        effect: int = 0
        match self.rarity:
            case "common":
                number_of_stats = 1
                effect = random.randrange(1, 5)
            case "rare":
                number_of_stats = 2
                effect = random.randrange(3, 10)
            case "epic":
                number_of_stats = 3
                effect = random.randrange(5, 15)
            case "legendary":
                number_of_stats = 4
                effect = random.randrange(7, 20)

        lucks = luck_calculation()

        damage_boost_luck = lucks[0]
        health_boost_luck = lucks[1]
        armor_boost_luck = lucks[2]

        user_luck = random.random()

        d_user_damage_luck = abs(
            user_luck-damage_boost_luck)
        d_user_health_luck = abs(
            user_luck-health_boost_luck)
        d_user_armor_luck = abs(
            user_luck-armor_boost_luck)

        for _ in range(number_of_stats):
            if d_user_damage_luck > d_user_health_luck and d_user_damage_luck > d_user_armor_luck:
                print("damage")
                self.damage_boost += effect
            elif d_user_health_luck > d_user_damage_luck and d_user_health_luck > d_user_armor_luck:
                print("health")
                self.max_hp_boost += effect
            elif d_user_armor_luck > d_user_damage_luck and d_user_armor_luck > d_user_health_luck:
                print("armor")
                self.armor_boost += effect
