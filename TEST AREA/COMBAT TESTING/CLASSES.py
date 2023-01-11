
import random

# ITEM CLASS


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
    summa = sum([damage_boost_luck, health_boost_luck, armor_boost_luck])

    damage_boost_luck = damage_boost_luck / summa
    health_boost_luck = health_boost_luck / summa
    armor_boost_luck = armor_boost_luck / summa

    stats_boost_porcentage = [damage_boost_luck,
                              health_boost_luck, armor_boost_luck]
    return stats_boost_porcentage


class Item(object):
    """
    ITEM CLASS
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
        Max Health Boost  : {self.health_boost} %
        Armor Boost       : {self.armor_boost} %
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
                effect = random.randrange(1, 15)
            case "legendary":
                number_of_stats = 3
                effect = random.randrange(5, 15)

        damage_boost_luck = luck_calculation()[0]
        health_boost_luck = luck_calculation()[1]
        armor_boost_luck = luck_calculation()[2]

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
                self.health_boost += effect
            elif d_user_armor_luck > d_user_damage_luck and d_user_armor_luck > d_user_health_luck:
                print("armor")
                self.armor_boost += effect


class Player(object):
    """
    ANVÄNDAREN
    """

    def __init__(self) -> None:

        # Player Status
        self.name: str = 'bob'
        self.player_lift: int = 3
        self.player_hp: int = 10
        self.player_damage: int = random.randint(5, 10)
        self.player_lvl: int = 1
        self.player_armor: int = random.randint(1, 3)
        self.player_debuff: list[int] = []
        self.player_inventory: dict = {

            'item 1': None,
            'item 2': None,
            'item 3': None,
            'item 4': None,
            'item 5': None,
        }


def get_items_from_inventory(inventory: dict) -> list[Item]:
    """

    Get all of the items from the player invenotry

    Args:
        inventory (dict): Player inventory

    Returns:
        LIst[Item]: retruns every items in the players inventory 
    """

    inventory_items: list[Item] = []
    p_inventory: list[tuple] = list(inventory.items())

    for (_, item) in (p_inventory):
        if isinstance(item, Item):
            inventory_items.append(item)
            continue
        pass
    return inventory_items


if __name__ == '__main__':
    player_1 = Player()

    print(player_1.player_inventory)

    item_1 = Item('rare', 'Item 1')
    player_1.player_inventory['item 1'] = item_1
    input()

    get_items_from_inventory(player_1.player_inventory)
