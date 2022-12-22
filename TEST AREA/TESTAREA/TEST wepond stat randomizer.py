
import random as r


def luck_calculation() -> list[float]:
    """
    HOW MUCH LUCK THE GAME HAVE
    """
    damage_boost_luck: float = 0
    armor_boost_luck: float = 0
    health_boost_luck: float = 0

    damage_boost_luck = r.random()
    armor_boost_luck = r.random()
    health_boost_luck = r.random()
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

    def __str__(self):

        return f"""
        
        damage boost: {self.damage_boost}
        health boost: {self.health_boost} 
        armor boost: {self.armor_boost}

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
                effect = r.randrange(0, 10)
            case "epic":
                number_of_stats = 2
                effect = r.randrange(0, 10)
            case "legendary":
                number_of_stats = 3
                effect = r.randrange(0, 10)

        damage_boost_luck = luck_calculation()[0]
        health_boost_luck = luck_calculation()[1]
        armor_boost_luck = luck_calculation()[2]

        user_luck = r.random()
        for _ in range(number_of_stats):
            if 0 < user_luck <= damage_boost_luck:
                self.damage_boost += effect
            elif damage_boost_luck < user_luck <= health_boost_luck:
                self.health_boost += effect
            elif health_boost_luck < user_luck <= armor_boost_luck:
                self.health_boost += effect


if __name__ == "__main__":
    pass
