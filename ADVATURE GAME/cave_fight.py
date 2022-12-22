from Game_classes import Player, Monster
from terminal_fixes import clearterminal


def combat_fighting_menu(player: Player, turn: int):
    """
    Player fighting monster Menu:
    """
    p_name: str = player.name
    p_hp: int = player.health
    p_dmg: int = player.damage
    p_lvl: int = player.level
    p_items: dict = player.inventory
    p_armor: int = player.armor

    match turn:
        case 1:
            monster = Monster(1)
        case 2:
            monster = Monster(2)
        case 3:
            monster = Monster(3)
        case 4:
            monster = Monster(4)
        case 5:
            monster = Monster(5)
        case 6:
            monster = Monster(6)
        case 7:
            monster = Monster(7)
        case 8:
            monster = Monster(8)
        case 9:
            monster = Monster(9)
        case 10:
            monster = Monster(10)

    m_name: str = monster.name
    m_hp: int = monster.health
    m_dmg: int = monster.damage
    m_armor: int = monster.armor
    m_tier: int = monster.moster_level
