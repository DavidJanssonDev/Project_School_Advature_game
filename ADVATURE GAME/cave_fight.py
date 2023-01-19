
from game_classes import Monster, Player, Item
from math import floor
from terminal_fixes import clearterminal
from Menu_user_checker import menu_answer_checker


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

    hp_buff = dmg_buff = armor_buff = 0

    for _, item in enumerate(inventory):
        hp_buff += item.health_boost
        dmg_buff += item.damage_boost
        armor_buff += item.armor_boost

    return [hp_buff, dmg_buff, armor_buff]


def combat_fighting_menu(player: Player) -> None:
    """
    Player fighting monster Menu:
    """
    monster = Monster(player.p_turn)
    m_armor: int = monster.armor
    m_health: int = monster.health
    m_name: string = monster.name
    m_damage: int = monster.damage

    p_turn: int = player.p_turn
    p_name: str = player.name
    p_health: int = player.player_hp
    p_dmg: int = player.player_damage
    p_lvl: int = player.player_lvl
    p_items: list = get_items_from_inventory(player.player_inventory)
    p_armor: int = player.player_armor
    p_debuffs: list[list] = player.player_debuff
    p_true_dmg: int = 0

    menu_options: list[str] = ['fight', 'use items', 'escape']
    while True:
        userawnser: str = ""
        while userawnser not in menu_options:
            clearterminal()
            userawnser = input(
                f"""
        =====================================================================
        |                       Fight the MONSTER!                          |
        |                                                   Turn: {p_turn}  |
        |===================================================================|
        |            Your stats                      Monster stats          |
        |      >>>>>>>>>>>>>>>>>>>>>>>          >>>>>>>>>>>>>>>>>>>>>>>     |
        |      < Name: {p_name}      >          < Name: {m_name}      >     |
        |      < Level: {p_lvl}      >          < Health: {m_health}  >     |
        |      < Health: {p_health}  >          < Damage: {m_damage}  >     |
        |      < Damage: {p_dmg}     >          < Armour: {m_armor}   >     |
        |      < Armour: {p_armor}   >          <                     >
        |      >>>>>>>>>>>>>>>>>>>>>>>          >>>>>>>>>>>>>>>>>>>>>>>     |



        |      <<<<<<<<<<<<<<<<<<<<<<<          <<<<<<<<<<<<<<<<<<<<<<<     |
        |                                                                   |
        |===================================================================|
        |   1.Fight                       |  Type:1/Fight                   |
        |   2.Use items                   |  Type:2/Use items               |
        |   3.Escape                      |  Type:3/Escape                  |
        =====================================================================
         """
            )
            userawnser = menu_answer_checker(userawnser, menu_options)
            match userawnser:
                case "fight":
                    pass
                case "Use items":
                    pass
                case "Escape":
                    are_you_sure: str = input(
                        "Are you sure you want to escape this time then write NO/Yes")
                    if are_you_sure.lower() == "yes":
                        player.player_life -= 1
                        return


print(p_items)
input()
