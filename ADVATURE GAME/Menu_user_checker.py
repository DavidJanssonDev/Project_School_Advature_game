

from time import sleep
from rich.progress import track

from terminal_fixes import clearterminal

ERROR_TID = 10  # Tiden som det tar för att anvädaren ska vänta


def menu_answer_checker(user_awnser: str, menu_op: list[str]) -> str:
    """
    Parameter:
        menu_op: list of menu options

        user_awnser: the string of the user awnser

    Return:

        user_checked_awnser (str)
    """
    user_awnser_int: int
    user_awnser_int_error: list[bool] = []
    user_awnser_str_error: list[bool] = []

    #! CHECKING SYMBOLS ERROR
    if user_awnser.isnumeric() or user_awnser.isalpha():

        #! CHECKING STR ERROR
        if user_awnser.isalpha():
            for option in menu_op:
                if user_awnser.lower() != option.lower():
                    user_awnser_str_error.append(False)
                else:
                    user_awnser_str_error.append(True)
            for index, ture_or_false in enumerate(user_awnser_str_error):
                if ture_or_false:
                    return menu_op[index]

            menu_error('Invaled menu option')
            return ''

        #! CHECKING INT ERROR
        user_awnser_int = int(user_awnser) - 1
        # * Lägger in i en lista vilka index som är giltiga
        for index in range(len(menu_op)):
            if user_awnser_int != index:
                user_awnser_int_error.append(False)
            else:
                user_awnser_int_error.append(True)

        for index, ture_or_false in enumerate(user_awnser_int_error):
            if ture_or_false:
                return menu_op[index]

        menu_error('Invaled number')
        return ''

    menu_error('No symbols')
    return ''


def menu_error(type_of_message: str) -> None:
    """
    MENU ERROR
    """

    clearterminal()
    print(
        f'Wait {ERROR_TID} secondes, before typeing a new awnser. Wrong type messege: {type_of_message}')
    for step in track(range(ERROR_TID)):
        sleep(1)
    clearterminal()
