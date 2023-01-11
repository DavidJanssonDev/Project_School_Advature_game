
from Game_classes import Monster
from Game_classes import Player
from Game_classes import Item
from terminal_fixes import clearterminal


def get_items_from_inventory(inventory: dict) -> list:
    """
    Takes every items from the players invetory

    Args:
        inventory (dict): Player inventory

    Returns:
        list: Returns a list of all of the items, if there are none the list is empty
    """
    items: list = []
    for (_, item) in enumerate(inventory.items()):
        if item == Item:
            items.append(item)
        else:
            pass
    return items


def damage_calculation(p_damage: int, p_inventory: list, p_debuffs: list[int]) -> int:
    """

    Calculate all of the damage a player does

    Args:
        player_damage (int): what base damage the player has
        player_inventory (dict): what inventory the player has
        player_debuffs (list): what debuffs the player has

    Returns:
        int: The True value of the player's damage
    """

    # Get the player item from inventroy

    return 1


def combat_fighting_menu(player):
    """
    Player fighting monster Menu:
    """
    P_NAME: str = player.name
    p_hp: int = player.player_hp
    p_dmg: int = player.player_damage
    p_lvl: int = player.player_lvl
    p_items: list = get_items_from_inventory(player.player_inventory)
    p_armor: int = player.player_armor
    p_debuffs: list[int] = player.player_debuff
    p_trueDamage: int = damage_calculation(p_dmg, p_items, p_debuffs)

    print(p_items)
    input()
