from rich.traceback import install

install


def menu_check(user_awnser: str, menu_op: list[str]) -> str:
    """
    Parameter:
        menu_op: list of menu options

        user_awnser: the string of the user awnser  

    Return:

    """
    user_awnser_int: int
    user_awnser_int_error: list[bool] = []
    user_awnser_str_error: list[bool] = []

    #! CHECKING SYMBOLS ERROR
    if user_awnser.isnumeric() or user_awnser.isalpha():

        #! CHECKING STR ERROR
        if user_awnser.isalpha():
            for option in menu_op:
                if user_awnser.lower() != option:
                    user_awnser_str_error.append(False)
                else:
                    user_awnser_str_error.append(True)
            for index, ture_or_false in enumerate(user_awnser_str_error):
                if ture_or_false:
                    return menu_op[index]
            # return 'you got a error [str]'

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
        # return 'you got a error [int]'

    # return 'you got a error [annat]'
