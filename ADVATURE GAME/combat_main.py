

import random

# * COMBAT SYSTEM
from combat_inventory import inventory_main_menu
from player_showoff import show_avatar_and_stats
from cave_menu import cave_menu

# * FUNKTIONER
from Menu_user_checker import menu_answer_checker
from terminal_fixes import clearterminal

# *CLASSES
from Game_classes import Player


def sure_to_play():
    """

    MAKEING SURE THAT THE USER WANTS TO PLAY

    """
    menu_options = ["start", "back"]
    game_is_runing = True
    clearterminal()
    while game_is_runing:
        userawnser = ""
        while userawnser not in menu_options:
            userawnser = input("""
=====================================================================

   _____ _______       _____ _______    _____          __  __ ______
  / ____|__   __|/\\   |  __ \\__   __|  / ____|   /\\   |  \\/  |  ____|
 | (___    | |  /  \\  | |__) | | |    | |  __   /  \\  | \\  / | |__
  \\___ \\   | | / /\\ \\ |  _  /  | |    | | |_ | / /\\ \\ | |\\/| |  __|
  ____) |  | |/ ____ \\| | \\ \\  | |    | |__| |/ ____ \\| |  | | |____
 |_____/   |_/_/    \\_\\_|  \\_\\ |_|     \\_____/_/    \\_\\_|  |_|______|


=====================================================================
        1. START THE GAME        | Type: GAME       /1
        2. BACK                  | Type: BACK       /2
=====================================================================
TYPE: """)
            userawnser = menu_answer_checker(
                userawnser, menu_options)
            match userawnser:
                case "start":
                    combat_main_menu()
                    return
                case "back":
                    return


def combat_main_menu():
    """

    MAIN MENU WHEN YOU ARE PLAYING THE GAME

    """
    player = player_creater()  # Create the player
    turn = 0
    menu_options = ["cave", "show", "inventory", "quit"]  # Options
    game_is_runing = True
    while game_is_runing:
        userawnser = ""
        while userawnser not in menu_options:
            clearterminal()
            userawnser = input(f"""
==============================================
                GAME MENU           {turn}
==============================================
  1. GO TO THE CAVE    | Type: CAVE      / 1
  2. SHOW AVATAR/STATS | Type: SHOW      / 2
  3. INVETORY          | Type: INVENTORY / 3
  4. QUIT              | Type: QUIT      / 4
============================================
TYPE: """)
            userawnser = menu_answer_checker(
                userawnser, menu_options)
            match userawnser:
                case "cave":

                    cave_menu(player)
                    turn += 1

                case "show":
                    show_avatar_and_stats(player)

                case "inventory":
                    inventory_main_menu(player.inventory)

                case "quit":
                    are_you_sure = input(
                        "Are you sure that you want to quit [YES/NO]? ")
                    match are_you_sure:
                        case "yes":
                            return
                        case "no":
                            continue


def player_creater() -> Player:
    """
    CREATING THE USER PLAYER

    Returns:
        _type_: _description_
    """
    base_blueproff_stats = {
        "Name": str,
        "Life": 3,
        "Health": 10,
        "Level": 1,
        "Armor": random.choice(["Heavyarmor", "Lightarmor"]),
        "Speed": random.randint(0, 10),
        "Damage": random.randint(5, 10),
    }

    base_blueproff_avatar = {
        "Skin color": str,
        "Hair color": str,
        "Body shape": str,
        "Eye color": str,
        "Height": int,
        "Weight": int
    }

    USER_OPTIONS = [
        "Name", "Skin color", "Hair color", "Body shape", "Eye color", "Height", "Weight"]
    INT_OPTOPN = ["Height", "Weight"]
    STR_OPTOPN = ["Skin color", "Hair color", "Body shape", "Eye color"]

    for option in USER_OPTIONS:
        name_awnser: str = ""
        str_awnser: str = ""
        int_awnser: str = ""
        clearterminal()

        # ? USER TYPES IN THERE NAME FOR THERE CHARACTER
        if option == "Name":
            while not name_awnser.isalpha():  # Makes sure that its only lether anwser goes throw
                name_awnser = input(
                    "Please enter your name character [only lethers]: ")
                base_blueproff_stats["Name"] = name_awnser

        # ? USER TYPES IN THERE AWNSERS TO THE STRING RELATED QUESTION
        elif option in STR_OPTOPN:
            while not str_awnser.isalpha():
                str_awnser = input(
                    f"What {option} does your character have [only lethers] ? ")
                base_blueproff_avatar[option] = str_awnser

        # ? USER TYPES IN THERE AWNSERS TO THE INTERGER RELATED QUESTION

        elif option in INT_OPTOPN:

            while not int_awnser.isnumeric():
                int_awnser = input(
                    f"What {option} does your character have[only numbers] ? ")
            base_blueproff_avatar[option] = int(int_awnser)
    return Player(base_blueproff_stats, base_blueproff_avatar)


if __name__ == "__main__":
    ewa = player_creater()
    ewa.print_player_avatar()
    ewa.print_player_stats()
