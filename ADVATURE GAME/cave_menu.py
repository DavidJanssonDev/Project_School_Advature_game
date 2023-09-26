"""
    WHERE ALL THE COMBAT MENU IS

"""


# Imports
import random


# Menu
from combat_inventory import item_place_empty_or_taken, dictunary_to_list
from cave_fight import combat_fighting_menu
from terminal_fixes import clearterminal
from falla import trap


# Player and classes
from Game_classes import Player, Item


def cave_menu(player: Player) -> None:
    """

    CAVE MAIN MENU

    """

    menu_options: list = ['1', '2', '3', 'back']
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
                    combat_fighting_menu(player)

                    return
                case 'chest':
                    combat_cave_chest_menu(player.player_inventory)
                    return
                case 'trap':
                    if len(player.player_debuff) == 3:
                        combat_fighting_menu(player)
                        return
                    trap(player)
                case 'back':
                    return


def cave_randomizing(userawnser: str) -> str:
    """

    Randomizar vilken cave avändaren ska gå i

    Args:
        userawnser (str): vad som använder har sagt

    Returns:
        str: Random cave mellan: nothing, monster, chest, trap
    """
    userawnser_cleen: str = userawnser.lower()
    cave_choice: str = ""

    if userawnser.isnumeric():

        if 1 <= int(userawnser_cleen) <= 3:
            cave_choice: str = random.choice(
                ['nothing', 'monster', 'chest', 'trap'])
        elif userawnser_cleen == "4":
            cave_choice: str = "back"

    if userawnser_cleen.isalpha():
        if userawnser_cleen.lower() == 'back':
            cave_choice: str = "back"

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
  There was nothing inside here in this cave

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
                    return
                case "2":
                    player_inventory["item 1"] = chest_item
                    return
                case "3":
                    player_inventory["item 1"] = chest_item
                    return
                case "4":
                    player_inventory["item 1"] = chest_item
                    return
                case "5":
                    player_inventory["item 1"] = chest_item
                    return
                case 'leave':
                    return
