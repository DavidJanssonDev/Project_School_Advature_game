import random


class Item:
    def __init__(self, rarity: str, name: str) -> None:
        self.rarity: str = rarity
        self.name: str = name
        self.item_stats: dict = {
            "Damage Multiplier": 0,
            "Max Health Boost": 0,
            "Armor Boost": 0
        }
        self.effect: str = f"""
            Damage Multiplier : {self.item_stats["Damage Multiplier"]}
            Max Health Boost  : {self.item_stats["Max Health Boost"]}
            Armor:            : {self.item_stats["Armor Boost"]}
        """
        self.stats_available: bool = True

    def __str__(self) -> str:
        return f"""

    This artefact is called {self.name} and has rarity of {self.rarity}

    Effected:

        Damage Multiplier : {self.item_stats["Damage Multiplier"]}
        Max Health Boost  : {self.item_stats["Max Health Boost"]} %
        Armor Boost       : {self.item_stats["Armor Boost"]} %

    """

    def stat_randomizer(self, rareity: str):
        max_min_damage_multiplier: tuple
        max_min_max_health_boost: tuple
        max_min_armor_boost: tuple


if __name__ == "__main__":
    item_1 = Item("rare", "hi")
    print(item_1)
