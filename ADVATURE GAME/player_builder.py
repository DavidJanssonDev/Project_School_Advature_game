from terminal_fixes import clearterminal
from Game_classes import Player


def player_creater():
    """
    CREATING THE USER PLAYER

    Returns:
        Player: USER PLAYER object
    """

    base_blueprint_avatar = {
        'user name': '',
        'skin color': '',
        'hair color': '',
        'body shape': '',
        'eye color': '',
        'height': 0,
        'weight': 0
    }
    print(f'\n\n{list(base_blueprint_avatar.items())} \n\n')

    for (key, value) in list(base_blueprint_avatar.items()):
        user_awnser: str = ""
        clearterminal()

        # CHECKING IF THE VALUE IS NOT THE RIGHT ONE TO THE COROSPORENT TYPE
        if isinstance(value, str):
            while not user_awnser.isalpha():
                user_awnser = input(
                    f'What {key} does your character have [TYPE ONLY LETTHERS] ? ')
        else:
            while not user_awnser.isnumeric():
                user_awnser = input(
                    f'What {key} does your character have [TYPE ONLY NUMBERS] ? ')
        # ADDING IT TO THE DICTIONARY

        base_blueprint_avatar[key] = user_awnser

    return Player(list(base_blueprint_avatar.items()))
