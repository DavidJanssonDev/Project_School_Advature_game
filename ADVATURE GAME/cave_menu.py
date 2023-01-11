# Imports
import random
from combat_inventory import item_place_empty_or_taken, dictunary_to_list
from cave_fight import combat_fighting_menu
from Game_classes import Player, Item
from terminal_fixes import clearterminal


def cave_menu(player: Player) -> None:
    """

    CAVE HUVUD MENU

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
                    combat_fighting_menu(player)
                case 'chest':
                    combat_cave_chest_menu(player.player_inventory)
                case 'trap':
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


# ===========================
#       CAVE MENU 3
# ===========================
