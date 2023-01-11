

# * COMBAT SYSTEM
from combat_inventory import inventory_main_menu
from player_showoff import show_avatar_and_stats
from cave_menu import cave_menu

# * FUNKTIONER
from Menu_user_checker import menu_answer_checker
from terminal_fixes import clearterminal

# *CLASSES
from player_builder import player_creater


def sure_to_play():
    """

    MAKEING SURE THAT THE USER WANTS TO PLAY

    """
    menu_options = ["start", "back"]
    game_is_runing = True
    clearterminal()
    while game_is_runing:
        clearterminal()
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
                    inventory_main_menu(player.player_inventory)

                case "quit":
                    are_you_sure = input(
                        "Are you sure that you want to quit [YES/NO]? ")
                    match are_you_sure:
                        case "yes":
                            return
                        case "no":
                            continue
