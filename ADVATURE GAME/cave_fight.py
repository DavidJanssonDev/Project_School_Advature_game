
from Game_classes import Monster
from Game_classes import Player
from Game_classes import Item
from terminal_fixes import clearterminal


def get_items_from_inventory(inventory: dict) -> list[Item]:
    """
    Takes every items from the players invetory

    Args:
        inventory (dict): Player inventory

    Returns:
        list: Returns a list of all of the items, if there are none the list is empty
    """
    items: list[Item] = []

    for (_, item) in list(inventory.items()):
        if isinstance(item, Item):
            items.append(item)
        else:
            pass
    return items


def items_to_buffs(inventory: list[Item]) -> tuple[int, int, int]:
    """
    Takes every item from the players items and combinds the items same type of buffs togheter

    Args:
        inventory (list[Item]): Player inventory items

    Returns:
        tuple[int, int, int]: every hp buff from i
    """

    hp_buff: int = 0
    dmg_buff: int = 0
    armor_buff: int = 0
    for _, item in enumerate(inventory):
        hp_buff += item.health_boost
        dmg_buff += item.damage_boost
        armor_buff += item.armor_boost

    return (hp_buff, dmg_buff, armor_buff)


def damage_calculation(p_damage: int, p_inventory: list[Item], p_debuffs: list[int], monster_buffs: int) -> int:
    """

    Calculate all of the damage a player does

    Args:
        player_damage (int): what base damage the player has
        player_inventory (dict): what inventory the player has
        player_debuffs (list): what debuffs the player has

    Returns:
        int: The True value of the player's damage
    """
    buffs_from_itmes: tuple[int, int, int] = items_to_buffs(p_inventory)

    return 1


def combat_fighting_menu(player: Player, monster: Monster):
    """
    Player fighting monster Menu:
    """
    m_armor: int = monster.armor

    p_name: str = player.name
    p_health: int = player.player_hp
    p_dmg: int = player.player_damage
    p_lvl: int = player.player_lvl
    p_items: list = get_items_from_inventory(player.player_inventory)
    p_armor: int = player.player_armor
    p_debuffs: list[int] = player.player_debuff
    p_trueDamage: int = damage_calculation(p_dmg, p_items, p_debuffs, m_armor)

    print(p_items)
    input()
