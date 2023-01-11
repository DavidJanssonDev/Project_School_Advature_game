
# IMPORTS

from Menu_user_checker import menu_answer_checker
from terminal_fixes import clearterminal


def print_out_inventory(inventory: dict) -> None:
    """
    SUMERY: Skriver ut alla items och keys par i en dictionary

    INVENOTRY(DICT): inventory för användaren

    RETUNS: None
    """

    for (key, value) in inventory.items():
        print(f'Item {key}:{value}')


def inventory_main_menu(inventory: dict) -> None:
    """
    INVENTORY MENU

    """

    inventory_menu_options = ['inspect', 'release', 'back']

    while True:
        userawnser = ''
        while userawnser not in inventory_menu_options:
            clearterminal()
            print("""
==============================================
                INVENTORY MENU
==============================================
""")
            print_out_inventory(inventory)
            userawnser = input("""
==============================================
    1. INSPECT ONE ITEM | TYPE: inspect     /1
    2. GO BACK          | TYPE: back        /2
==============================================
Type:""")
            userawnser = menu_answer_checker(
                userawnser, inventory_menu_options)

            match userawnser:
                case'inspect':
                    inventory_inspect(inventory)

                case'back':
                    return


def dictunary_to_list(inventory: dict):
    """
    Gör en lista med alla vapen som avändaren ska ha till att välja
    i inspcterings meny

    Args:
        inventory (list): Användarens inventory

    Returns:
        list: Meny möjligheterna
    """

    temp_list: list = []

    for (item, _) in inventory.items():
        temp_list.append(str(item))
    temp_list.append('back')

    return temp_list


def inventory_inspect(inventory: dict) -> None:
    """
    Select panel för vilket som avändaren ska inspectera

    Args:
        inventory (list): Användarens inventory
    """

    menu_option: list = dictunary_to_list(inventory)

    while True:
        user_awnser = ''
        while user_awnser not in menu_option:
            clearterminal()
            print("""
==============================================
                INSPECT MENU
==============================================
""")
            # * PRINTS OUT EVERY ITEM
            print_out_inventory(inventory)

            user_awnser = input("""
==========================================================
                TYPE: NUMBER of witch item
                            Or
                TYPE: BACK to go back to inventory
=========================================================
Type:""")
            match user_awnser:
                case'1':
                    print_item_effect(inventory, 'item 1')
                    clearterminal()
                case'2':
                    print_item_effect(inventory, 'item 2')
                    clearterminal()
                case'3':
                    print_item_effect(inventory, 'item 3')
                    clearterminal()
                case'4':
                    print_item_effect(inventory, 'item 4')
                    clearterminal()
                case'5':
                    print_item_effect(inventory, 'item 5')
                    clearterminal()
                case'back':
                    return


def print_item_effect(inventory: dict, item: str) -> None:
    """

    Printar ut Item effect och namn

    Parameter:
        inventory (list): Användarens inventory
        Item (str): Vilket item i invenoty
    """

    if inventory[item] is not None:
        item_effect = inventory[item].effect
        item_name = inventory[item].name
    else:
        item_effect = None
        item_name = None

    clearterminal()
    print(f"""
==============================================

    ITEM NAME:{item_name}

    ITEM STATS: {item_effect}
           """)
    input("""
==============================================
           | PRESS ENTER TO GO BACK |
==============================================
""")


def item_place_empty_or_taken(inventory: dict) -> None:
    """
    Prints ut vilka av de itemslotsen som är tillgängliga 

    Args:
        inventory (dict): Användarens inventory
    """
    for item in inventory.items():
        if item is None:
            print("▢", end="")
        else:
            print("▣", end="")
