
from terminal_fixes import clearterminal
from Menu_user_checker import menu_answer_checker


# * MENU FOR SHOWING THE USER THE AVATAR/STATS
def show_avatar_and_stats(player):
    """

    MENU OF ETHER SHOWING THE USER AVATAR OR THE USER STATS

    """

    menu_options = ["avatar", "stats", "back"]

    while True:

        userawnser = ""
        while userawnser not in menu_options:
            clearterminal()
            userawnser = input("""
==============================================
                SHOW MENU
==============================================
1. SHOW AVATAR    | Type: avatar   / 1
2. SHOW STATS     | Type: stats    / 2
3. GO BACK        | Type: back     / 3
============================================
TYPE: """)
            userawnser = menu_answer_checker(
                userawnser, menu_options)
            match userawnser:
                case "avatar":
                    display_user_stats(player)

                case "stats":
                    clearterminal()
                    player.print_player_stats()
                    input("""
==============================================
           | PRESS ENTER TO GO BACK |
==============================================
                          """)
                case "back":
                    return


def display_user_avatar(player):
    """

    DISPLAYS THE USER AVATAR

    """
    clearterminal()
    player.print_player_avatar()
    input("""
==============================================
           | PRESS ENTER TO GO BACK |
==============================================
            """)


def display_user_stats(player):
    """

    DISPLAYS THE USER STATUS

    """
    clearterminal()
    player.print_player_stats()
    input("""
==============================================
           | PRESS ENTER TO GO BACK |
==============================================
                          """)
