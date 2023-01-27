"""
    FIGHTING MENU

    Where the battel between the player and the moster happends

"""
# Other imports
import random
from math import floor
from time import sleep
from tabulate import tabulate


# Imports form files
from falla import de_buff_check
from game_classes import Monster, Player, Item
from Menu_user_checker import menu_answer_checker
from terminal_fixes import clearterminal


# Menyer


def dict_to_list(dictionary: dict) -> list[list[tuple[int, str]]]:
    """
    dictionary to list

    Args:
        dictionary(dict): dictionary of all the potion amout to the repectiv type
    """
    temp_list: list = []
    for (item, amount) in dictionary.items():
        temp_list.append([item, amount])

    return temp_list


def use_postion(type_of_postion: str, player: Player) -> None:
    """
    User drinks there posiions
    """
    player.player_potions[type_of_postion] -= 1
    player.drink_potions(type_of_postion)
    clearterminal()
    print(f"""
     | ====================================================== |
     |                                                        |
     |        YOU HAVE JUST DRANK A {type_of_postion.upper()} BOOST POSION       |
     |                                                        |
     | ====================================================== |
                              """)
    sleep(5)


def no_postion_menu() -> bool:
    """
    IF the user dont have any posions
    """
    useranwser: str
    meanu_options: list[str] = ['postion', 'fight']

    while True:
        useranwser: str = ''
        clearterminal()
        while useranwser not in meanu_options:
            useranwser: str = input("""
     | ====================================================== |
     |                                                        |
     |        YOU HAVE NO AMOUNT OF THAT POSTION LEFT         |
     |                                                        |
     | ====================================================== |
     |                                                        |
     |  OPTIONS:                                              |
     |                                                        |
     | 1) GO BACK AND CHOSE A NEW POSION [WRITE: POSTION / 1] |
     | 2) GO BACK AND BATTLE THE FIGHT   [WRITE: FIGHT   / 2] |
     |                                                        |
     |                                                        |
     | ====================================================== |
       TYPE: """).lower()
            you_have_no_posion_awnser = menu_answer_checker(
                useranwser, meanu_options)
            match you_have_no_posion_awnser:
                case "postion":
                    return True
                case "fight":
                    return False


def potion_menu(player: Player) -> None:
    """

    User use item menu

    Args:
        player_postions (dict[str, int]): player postions
    """
    menu_options: list[str] = ['damage', 'armor', 'health', 'back']
    list_of_amout_posions: list[list[tuple[int, str]]] = dict_to_list(
        player.player_potions)  # health, damage, armor

    while True:
        clearterminal()
        userawnser: str = ""
        while userawnser not in menu_options:
            userawnser = input(f"""

           | ===================================================== |
           |                     USER ITEM USE                     |
           | ===================================================== |
           |                                                       |
           | damage posions amount: {list_of_amout_posions[1][1]:<31}|
           | Armor  posions amount: {list_of_amout_posions[2][1]:<31}|
           | health posions amount: {list_of_amout_posions[0][1]:<31}|
           |                                                       |
           |= = = = = = = = = = = = = = = = = = = = = = = = = = = =|
           |                                                       |
           |     Which posions do you want to choose?              |
           |                                                       |
           |     1. Damage boost       > (Write: damage /1)        |
           |     2. Armor boost        > (Write: armor  /2)        |
           |     3  Health regin       > (Write: health /3)        |
           |     4. back               > (Write: back   /4)        |
           |                                                       |
           | ===================================================== |

            TYPE: """)
            userawnser = menu_answer_checker(userawnser, menu_options)

            match userawnser:
                case "damage":
                    if list_of_amout_posions[1][1][0] >= 0:
                        use_postion("damage", player)
                        return
                    no_postion_menu()
                    continue

                case"armor":
                    if list_of_amout_posions[2][1][0] >= 0:
                        use_postion(",armor", player)
                        return
                    no_postion_menu()
                    continue

                case "health":
                    if list_of_amout_posions[0][1][0] >= 0:
                        use_postion("health", player)
                        return
                    no_postion_menu()
                    continue

                case "back":
                    return


def potions_checker(player: Player) -> None:
    """
    Checks if the potion that the player have is still activ

    Args:
        player_turn (int): player current turn
        player_buffs (list[list]): the player buffs
    """

    for index, type_of_list in enumerate(player.player_buff):
        if type_of_list[2] == player.p_turn:
            player.player_buff.pop(index)
        else:
            pass

# STATS EFFECTER


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


def items_to_buffs(player: Player) -> list[tuple[int, str]]:
    """
    Takes every item from the players items and combinds the items same type of buffs togheter

    Args:
        inventory (list[Item]): Player inventory items

    Returns:
        tuple[int, int, int]: every hp buff from i
    """
    p_items: list[Item] = get_items_from_inventory(player.player_inventory)
    dmg_buff: int = 0
    armor_buff: int = 0
    max_hp_buff: int = 0

    for _, item in enumerate(p_items):
        max_hp_buff *= item.max_hp_boost
        dmg_buff *= item.damage_boost
        armor_buff *= item.armor_boost

    return [(max_hp_buff, 'health'), (dmg_buff, 'damage'), (armor_buff, 'armor')]


def apply_all_buff_to_player(player: Player) -> None:
    """
    Args:
        player_debuffs (list[list]): _description_
        player_buffs (list[list]): _description_

    Returns:
        list[float]: _description_
    """
    potions_checker(player)
    de_buff_check(player)

    player_buffs: list = player.player_buff
    player_debuffs: list = player.player_debuff
    player_items_buff: list = items_to_buffs(player)

    player_all_buffs: list = player_buffs + player_items_buff + player_debuffs

    dmg_buff: float = 1
    health_buff: float = 1
    armor_buff: float = 1

    for _, item in enumerate(player_all_buffs):

        if isinstance(item, list):

            match item[0]:
                case 'damage':
                    dmg_buff *= item[1]

                case 'health':
                    health_buff *= item[1]

                case 'armor_buff':
                    armor_buff *= item[1]
        else:
            match item:
                case 'damage':
                    dmg_buff *= item[0]/100

                case 'health':
                    health_buff *= item[0]/100

                case 'armor':
                    armor_buff *= item[0]/100

    player.player_hp = floor(player.player_max_hp * health_buff)
    player.player_damage = floor(player.player_damage * dmg_buff)
    player.player_armor = floor(player.player_armor * armor_buff)


def do_damage(player: Player, monster: Monster, whos_trun: str):
    """

    Makes the damage

    Args:
        player (Player): Player
        monster (Monster): Monster
        whos_trun (str): who has teh turn
    """

    player_base_damage = player.player_damage
    monster_base_damage = monster.damage

    monster_armor = 1-(monster.armor/100)
    player_armor = 1-(player.player_armor/100)

    match whos_trun.lower():

        case 'player':

            monster.health -= damage(player_base_damage, monster_armor)

        case 'monster':

            player.player_hp -= damage(monster_base_damage, player_armor)


def damage(base_damage: int, armor: float) -> int:
    """
    Damage that monster or player do

    Args:
        base_damage (int): base damage or player
        monster_armor (float): armor for monster or player

    Returns:
        int: the damage that the player or monster do
    """
    return round(base_damage*armor)


def combat_fighting_menu(player: Player) -> None:
    """
    Player fighting monster Menu:
    """
    monster = Monster(player.player_lvl)
    monster.stat_change()

    m_armor: int = monster.armor
    m_health: int = monster.health
    m_name: str = monster.name
    m_lvl: int = monster.moster_level

    p_name: str = player.name
    p_health: int = player.player_hp

    p_lvl: int = player.player_lvl
    p_armor: int = player.player_armor

    p_true_dmg: int = damage(player.player_damage, monster.armor)
    m_true_dmg: int = damage(monster.damage, player.player_armor)

    menu_options: list[str] = ['fight', 'items', 'escape']
    while True:

        m_armor: int = monster.armor
        m_health: int = monster.health
        m_name: str = monster.name
        m_lvl: int = monster.moster_level

        p_name: str = player.name
        p_health: int = player.player_hp

        p_lvl: int = player.player_lvl
        p_armor: int = player.player_armor

        p_true_dmg: int = damage(player.player_damage, monster.armor)
        m_true_dmg: int = damage(monster.damage, player.player_armor)

        userawnser: str = ""

        clearterminal()
        apply_all_buff_to_player(player)
        while userawnser not in menu_options:
            print("""
|=====================================|
|          Fight the MONSTER!         |
|=====================================|
        """)
            DISPLAY_FIGHT_MENU = [
                [f'PLAYER: {p_name}', '| VS |', f'MONSTER {m_name}'],
                [f'Level: {p_lvl}', '', f'Level:{m_lvl}'],
                [f'Health: {p_health}', '', f'Health{m_health}'],
                [f'Damage: {p_true_dmg}', '', f'Damage{m_true_dmg}'],
                [f'Armor: {p_armor}', '', f'Armor: {m_armor}']]

            print(tabulate(DISPLAY_FIGHT_MENU, headers="firstrow", tablefmt="psql"))
            userawnser = input(""" 
|=====================================|
|   1.Fight      |  Type:1/Fight      |
|   2.Use items  |  Type:2/Use items  |
|   3.Escape     |  Type:3/Escape     |
|=====================================|
TYPE: """)
            userawnser = menu_answer_checker(userawnser, menu_options)
            match userawnser:
                case "fight":
                    battel_fight(player, monster)
                case 'items':
                    potion_menu(player)

                case "escape":
                    are_you_sure: str = input(
                        "Are you sure you want to escape this time then write NO/Yes")
                    if are_you_sure.lower() == "yes":
                        player.player_life -= 1
                        return
        if monster.health <= 0:
            player.player_lvl += 1
            player.p_turn += 1
            player.level_up()
            return
        if player.player_hp <= 0:
            player.player_life -= 1
            player.p_turn += 1
            return


def battel_fight(player, monster) -> None:
    """

    The accual fight when doing damage

    """
    do_monster_attack: bool = random.choice([True, False])

    if do_monster_attack:
        do_damage(player, monster, 'monster')

    do_damage(player, monster, 'player')
