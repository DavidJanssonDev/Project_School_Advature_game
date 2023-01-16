
from Game_classes import Monster
from Game_classes import Player
from Game_classes import Item
from math import floor
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


def items_to_buffs(inventory: list[Item]) -> list[int]:
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

    return [hp_buff, dmg_buff, armor_buff]


def debuffs_to_int(debuffs: dict[str, int]) -> list[float]:
    """
    Takes every debuffs out of the player class dictarnary and adds them together

    Args:
        debuffs (dict[str, int]): _description_

    Returns:
        list[float]: List of all the types of debuffs
    """
    p_debuff_dmg: float = 0
    p_debuff_hp: float = 0
    p_debuff_armor: float = 0
    for (name_of_buff, buff) in enumerate(list(debuffs.items())):
        if name_of_buff == 'damage':
            p_debuff_dmg += buff[1]
        elif name_of_buff == 'health':
            p_debuff_hp += buff[1]
        elif name_of_buff == 'armor':
            p_debuff_armor += buff[1]
    return [p_debuff_hp, p_debuff_dmg, p_debuff_armor]


def damage_calculation(p_dmg: int, p_in: list[Item], p_debuff: dict[str, int], m_armor: int) -> int:
    """

    Calculate all of the damage a player does

    Args:
        p_dmg (int): what base damage the player has
        p_in (dict): what inventory the player has
        p_debuffs (list): what debuffs the player has
        m_armor (int): monster armor

    Returns:
        int: The True value of the player's damage
    """
    buffs_from_itmes: list[int] = items_to_buffs(p_in)
    player_buffs: float = buffs_from_itmes[1] - p_debuff['damage']
    player_damage: int = floor(p_dmg * player_buffs * (m_armor/100))
    return player_damage


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
    p_debuffs: dict[str, int] = player.player_debuff
    p_true_dmg: int = damage_calculation(p_dmg, p_items, p_debuffs, m_armor)

    print(p_items)
    input()
