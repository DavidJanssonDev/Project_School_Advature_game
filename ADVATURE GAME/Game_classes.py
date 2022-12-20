
import random
from tabulate import tabulate

# ============================================================================
#                              PLAYER
# ============================================================================


class Player:
    """
    THE USER PLAYER
    """

    def __init__(self, player_stats: dict, player_looks: dict) -> None:
        self.player_looks = player_looks  # Alla karatiskiska saker som en användare har
        self.name = player_stats.get("Name")
        self.level = player_stats.get("Level")
        self.armor = player_stats.get("Armor")
        self.damage = player_stats.get("Damage")
        self.health = player_stats.get("Health")
        self.life = player_stats.get("Life")
        self.inventory = {"Item 1": None, "Item 2": None,
                          "Item 3": None, "Item 4": None, "Item 5": None}

    def print_player_stats(self):
        """
        Prints out a table of how the player looks
        """
        table_stats_data = [
            ["Player Stats", ""],
            ["Name", self.name],
            ["Life", self.life],
            ["Level", self.level],
            ["Health", self.health],
            ["Damage", self.damage],
            ["Armor", self.armor]
        ]
    # FUNCTION FOR PRINTING OUT THE PLAYER STATS
        print(tabulate(table_stats_data, headers="firstrow", tablefmt="psql"))

    def print_player_avatar(self):
        """
        Prints out a player avatar looks
        """

        table_stats_avatar = [
            ["Avatar", ""],
            ["Skin color", self.player_looks.get("Skin color")],
            ["Hair color", self.player_looks.get("Hair color")],
            ["Body shape", self.player_looks.get("Body shape")],
            ["Eye color", self.player_looks.get("Eye color")],
            ["Height", self.player_looks.get("Height")],
            ["Weight", self.player_looks.get("Weight")],
        ]
    # FUNCTION FOR PRINTING OUT THE PLAYER LOOKS
        print(tabulate(table_stats_avatar, headers="firstrow", tablefmt="psql"))

# ============================================================================
#                               MONSTER
# ============================================================================


class Monster:
    """

    MONSTER FOR A PLAYER, EMENY THAT PLAYER WILL FIGHT IN THE GAME

    """

    def __init__(self, monster_stats_tier: int) -> None:
        self.monster_stats_tier = monster_stats_tier

        if monster_stats_tier == 1:
            self.name = "Bob"
            self.health = 10
            self.damage = 5
            self.armor = 0
            self.speed = random.randint(0, 15)
        if monster_stats_tier == 2:
            self.name = "Bob 2.0"
            self.health = 25
            self.damage = 7
            self.armor = 2
            self.speed = random.randint(10, 20)


# ============================================================================
#                               CHEST
# ============================================================================

def luck_calculation() -> list[float]:
    """
    HOW MUCH LUCK THE GAME HAVE
    """
    damage_boost_luck: float = 0
    armor_boost_luck: float = 0
    health_boost_luck: float = 0

    damage_boost_luck = random.random()
    armor_boost_luck = random.random()
    health_boost_luck = random.random()
    lista_num = [damage_boost_luck, health_boost_luck, armor_boost_luck]
    summa = sum(lista_num)

    damage_boost_luck = damage_boost_luck / summa
    health_boost_luck = health_boost_luck / summa
    armor_boost_luck = armor_boost_luck / summa

    stats_boost_porcentage = [damage_boost_luck,
                              health_boost_luck, armor_boost_luck]
    return stats_boost_porcentage


class Item(object):
    """
    item
    """

    def __init__(self, rarity: str, item_name: str) -> None:
        self.rarity = rarity
        self.item_name = item_name

        self.damage_boost: int = 0
        self.health_boost: int = 0
        self.armor_boost: int = 0

    def __str__(self) -> str:
        return f"""

    This artefact is called {self.item_name} and has rarity of {self.rarity}

    Effected:

        Damage Multiplier : {self.damage_boost}
        Max Health Boost  : {self.damage_boost} %
        Armor Boost       : {self.damage_boost} %
    """

    def genatate_stat(self):
        """
        somthing
        """
        number_of_stats: int = 0
        effect: int = 0
        match self.rarity:
            case "rare":
                number_of_stats = 1
                effect = random.randrange(0, 10)
            case "epic":
                number_of_stats = 2
                effect = random.randrange(0, 10)
            case "legendary":
                number_of_stats = 3
                effect = random.randrange(0, 10)

        damage_boost_luck = luck_calculation()[0]
        health_boost_luck = luck_calculation()[1]
        armor_boost_luck = luck_calculation()[2]

        user_luck = random.random()

        for _ in range(number_of_stats):
            if 0 < user_luck <= damage_boost_luck:
                self.damage_boost += effect
            elif damage_boost_luck < user_luck <= health_boost_luck:
                self.health_boost += effect
            elif health_boost_luck < user_luck <= armor_boost_luck:
                self.health_boost += effect
