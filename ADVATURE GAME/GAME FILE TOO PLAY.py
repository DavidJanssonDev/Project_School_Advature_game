
# RICH
from rich.traceback import install


# IMPORTS FROM OTHER FILES
from How_To_play_menu import how_to_play_main_menu
from combat_main import sure_to_play

# Menu utilitys
from terminal_fixes import clearterminal
from Menu_user_checker import menu_answer_checker


install()


#*====== GAME FUNCTION ======*#


def main():
    """

    THIS IS THE MEIN FUNCTION THAT ALAWDS YOU TO PLAY THE GAME

    """
    menu_options = ["game", "how", "quit"]
    game_running: bool = True
    while game_running:
        userawnser: str = ""

        while userawnser not in menu_options:
            clearterminal()
userawnser = input("""
==============================================
                  MAIN MENU
==============================================
  1. PLAY GAME        | Type: GAME        /1
  2. HOW TO PLAY      | Type: HOW         /2
  3. QUIT             | Type: QUIT        /3
==============================================
TYPE: """)
userawnser = menu_answer_checker(userawnser, menu_options)
            match userawnser:
                case "game":
                    sure_to_play()

                case "how":
                    how_to_play_main_menu()

                case "quit":
                    are_you_sure = input(
                        "Are you sure that you want to quit [YES/NO]? ")
                    match are_you_sure:
                        case "yes":
                            game_running = False
                        case"no":
                            continue


if __name__ == '__main__':
    main()
