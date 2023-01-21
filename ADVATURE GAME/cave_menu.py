# Imports
from math import floor, ceil
import random
from combat_inventory import item_place_empty_or_taken, dictunary_to_list
from cave_fight import combat_fighting_menu
from game_classes import Player, Item
from terminal_fixes import clearterminal


def cave_menu(player: Player) -> None:
    """

    CAVE MAIN MENU

    """

    menu_options: list = ['1', '2', '3', '4']
    while True:
        userawnser: str = ""
        while userawnser not in menu_options:
            clearterminal()
            userawnser = input("""
==============================================
                  MAIN MENU
==============================================
  1. CAVE 1           | Type: Cave 1      /1
  2. CAVE 2           | Type: Cave 2      /2
  3. CAVE 3           | Type: Cave 3      /3
  4. BACK             | Type: BACK
==============================================
TYPE: Cave """)
            userawnser = cave_randomizing(userawnser)

            match userawnser.lower():
                case 'nothing':
                    combat_cave_nothing_menu()
                    return
                case 'monster':
                    combat_fighting_menu(player, )
                    return
                case 'chest':
                    combat_cave_chest_menu(player.player_inventory)
                    return
                case 'trap':
                    if len(player.player_debuff) == 3:
                        combat_fighting_menu(player, )
                        return
                    else:
                        print('Trap was here')
                        input('')


def cave_randomizing(userawnser: str) -> str:
    """

    Randomizar vilken cave avändaren ska gå i

    Args:
        userawnser (str): vad som använder har sagt

    Returns:
        str: Random cave mellan: nothing, monster, chest, trap
    """
    cave_choice: str = ""
    user_in_range: bool = userawnser.isnumeric() and (1 <= int(userawnser) <= 3)

    if userawnser.isalpha():
        if userawnser.lower() == 'back':
            return 'back'

    if user_in_range:
        cave_choice = random.choice(['nothing', 'monster', 'chest', 'trap'])
    return cave_choice

# ===========================
#       CAVE MENU 1
# ===========================


def combat_cave_nothing_menu() -> None:
    """

    Vad som händer när man kommer till nothing menyn

    """
    clearterminal()
    input("""
==============================================

     Watch how lucky you were this time!
  There was nothing inside here in the cave

==============================================
       """)


# ===========================
#       CAVE MENU 2
# ===========================

def combat_cave_chest_menu(player_inventory: dict) -> None:
    """
    Menu where the user get a item
    """

    item_names = ['Lucky Mask', 'Anarchy Rod',
                  'Hellish Band', 'Seduction Shard',
                  'Fates Microlith', 'Statuette of Mysteries',
                  'Cloak of Affluence', 'Runes of Greed',
                  'Rod of Malice', 'Slab of Bane',
                  ]

    random_rarity_of_weapons = random.choice(['rare', 'epic', 'legendary'])
    random_name_of_weapons = random.choice(item_names)

    chest_item = Item(random_rarity_of_weapons.lower(),
                      random_name_of_weapons.lower())

    chest_item.genatate_stat()

    menu_options = dictunary_to_list(player_inventory)

    while True:
        userawnser: str = ''
        while userawnser not in menu_options:
            clearterminal()
            print(f"""
==============================================
                  CHEST MENU
==============================================

YOU FOUND A {random_rarity_of_weapons} ITEM

    ITEM: {random_name_of_weapons}

    STATS: {chest_item}""")

            item_place_empty_or_taken(player_inventory)

            userawnser = input("""
==============================================
Wich of the slots do you want to place it in ?
                    OR
     Do you want to leave it and move on
==============================================
TYPE: Slot [number] or Leave it [leave]  """)

            match userawnser.lower():

                case "1":
                    player_inventory["item 1"] = chest_item
                case "2":
                    player_inventory["item 1"] = chest_item
                case "3":
                    player_inventory["item 1"] = chest_item
                case "4":
                    player_inventory["item 1"] = chest_item
                case "5":
                    player_inventory["item 1"] = chest_item
                case 'leave':
                    return
# ===========================
#       CAVE MENU 3
# ===========================


def tap_calc(rund_effect: float, curret_turn: int, effect_type: str):
    """

    Calculates the damage and the turns the debuff effect last

    Returns:
        int:
    """

    d_buff: float = 0
    d_buff_time: int = random.randint(1, 2) + curret_turn
    d_buff_temp: int = (pow(curret_turn, rund_effect) + 0.5)*10
    d_buff_str: str = str(d_buff_temp)
    descimal_int: str = d_buff_str[3]

    if int(descimal_int) >= 5:
        d_buff: float = ceil(int(d_buff_str))/10

    elif int(descimal_int) >= 5:
        d_buff: float = floor(int(d_buff_str))/10

    return [effect_type, d_buff,  d_buff_time]


def de_buff_check(player: Player) -> None:
    """

    Summery:

        Checks if the user d-buffs has run out 

    Parameter:

        player (Player): User player
    """
    curret_turn: int = player.p_turn
    debuffs: list[list] = player.player_debuff

    for index, numberlist in enumerate(debuffs):
        if numberlist[2] == curret_turn:
            debuffs.pop(index)


def trap(player: Player) -> None:
    """
    Funktion för det som händer när man har hamnat i en fälla.


    [['vad för debuff', effect, end rundda], ['vad för debuff', effect, end rundda], ['vad för debuff', effect, end rundda]]


    Args:
        player (Player): spelare klass
    """
    current_turn = player.p_turn
    effect: list = []
    random_deffect: str = random.choice(['health', 'damage', 'armor'])
    rund_effect: float
    current_d_buffs: list[list] = player.player_debuff

    match random_deffect:

        case 'health':
            rund_effect: float = 1.388
            effect = tap_calc(rund_effect, current_turn, random_deffect)
        case 'armor':
            rund_effect: float = 1.0682
            effect = tap_calc(rund_effect, current_turn, random_deffect)

        case 'damage':
            rund_effect: float = 1.6245
            effect = tap_calc(rund_effect, current_turn, random_deffect)

    current_d_buffs.append(effect)
