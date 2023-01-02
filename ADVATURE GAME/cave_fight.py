
from Game_classes import Monster
from Game_classes import Player
from terminal_fixes import clearterminal


def damage_calculation(player_damage: int, player_inventory: dict, player_deeffects: list) -> int:

    return 1


def combat_fighting_menu(player: Player, monster: Monster, turn: int):
    """
    Player fighting monster Menu:
    """
    p_name = player.name
    p_hp = player.health
    p_dmg: int = player.damage
    p_lvl = player.level
    p_items = player.inventory
    p_armor = player.armor
    p_deeffects = player.deeffects
    p_trueDamage = damage_calculation(p_dmg, p_items, p_deeffects)

    m_name = monster.name
    m_hp = monster.health
    m_dmg = monster.damage
    m_armor = monster.armor
    m_tier = monster.moster_level
