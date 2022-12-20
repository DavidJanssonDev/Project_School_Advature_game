

#!===== IMPORTS ====!#
from tabulate import tabulate
from Menu_user_checker import menu_answer_checker
from terminal_fixes import clearterminal
#^====== FUNKTIONER ======^#


def how_to_play_main_menu():
    """

    THIS IS THE MAIN MENU WHEN LOOKING HOW TO PLAY

    """
    menu_options = ["combat", "game play", "stats", "quit"]
    while True:
        userawnser = ""
        while userawnser not in menu_options:
            clearterminal()
            userawnser = input("""
==============================================
                HOW TO PLAY MENU
==============================================
  1. COMBAT           | Type: COMBAT
  2. GAME PLAY        | Type: GAME PLAY
  3. STATS            | Type: STATS
  4. QUIT             | Type: QUIT
==============================================
TYPE: """)
            userawnser = menu_answer_checker(
                userawnser, menu_options)

            match userawnser:

                case "combat":
                    display_how_combat_works()
                case "game play":
                    display_how_game_play_works()
                case "stats":
                    display_how_stats_works()
                case "quit":
                    return


def display_how_combat_works():
    pass


def display_how_game_play_works():
    """
    DISPLAYS THE LORE AND HOW THE GAME IS GOING TO WORK FOR THE USER

    """
    clearterminal()
    player_know_game = input(
        "Do you know how to play the game? [Yes/No]: ")

    if player_know_game.lower() != "yes":
        clearterminal()
        input("""
=======================================================================================================================
        You are a adventurer. Yes...you! And in someway you ended up in a dark cave middle of nowwhere. 
        You think you are lonely by yourself in a dark cave yes? No no no...it isn't...it isn't just you.
        There are monsters to! And to battle them you se a sword on the ground that you take with you. On the way 
        you will find chests with different items and relics that may help you survive. You will always have
        three chooises, three tunnels you can choose between. One of them could have a chest another one of them could
        be a trap or even a monster, you never know. You only have three lives and you need to be carefull. 
        You start on level zero. And when you are at level ten then the monsters let you out from the cave. 
        You can always se how many HP you have and which items you have been collected on the way and more. 
        I wish you all luck down there knight good luck.

=======================================================================================================================
                                         | PRESS ENTER TO GO BACK |
=======================================================================================================================
        """)


def display_how_stats_works():
    """
    TELLS THE USER WHAT EVERY STAT DO

    """
    table_Stats_Data = [
        ["Player Stats", ""],
        ["Name", "This is the name of your character"],
        ["Life", "This is the amount of Life overall you have and how many times you can die before you lose"],
        ["Level", "This is the level of your character"],
        ["Health", "This is how much health you have, if this goes to zero you are dead"],
        ["Damage", "This determents how much damage you deal"],
        ["Armor", "This reduce the damage take by how the amount of armor you have by 50%"],
        ["Items in inventory", "How many items you have in your inventory"],
    ]
    clearterminal()
    print("""
==============================================
          """)
    print(tabulate(table_Stats_Data, headers="firstrow", tablefmt="psql"))
    input("""
==============================================
           | PRESS ENTER TO GO BACK |
==============================================
          """)
