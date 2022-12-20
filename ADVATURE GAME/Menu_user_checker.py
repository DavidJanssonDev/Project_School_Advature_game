

from time import sleep
from rich.progress import track

from terminal_fixes import clearterminal


def menu_answer_checker(org_awnser: str, menu_options: list) -> str:
    """

    COMPARE THE USER AWNSER IF IT MATCHES THE MENU OPTIONS

    IF NOT IT TOO ASK THE USER TO TYPE A NEW AWNSER UNTILL IT HAS IT RIGHT

    """
    while True:
        if org_awnser.isalpha():
            for menu_item in menu_options:
                if menu_item.lower() == org_awnser.lower():
                    return org_awnser.lower()

        elif org_awnser.isnumeric():
            org_awnser = int(org_awnser)-1  # type: ignore
            for index in range(len(menu_options)):
                if org_awnser == index:
                    return menu_options[int(org_awnser)]
        else:
            clearterminal()
            print('YOU TYPED WORNG!!!')
            for steg in track(range(10)):
                sleep(1)

            clearterminal()
            print("Menu options:")
            for index, option in enumerate(menu_options):
                print(f'{index}:{option}')
            org_awnser = input("""Please type a new input: """)
