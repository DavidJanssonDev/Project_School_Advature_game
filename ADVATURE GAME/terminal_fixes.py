import os


def clearterminal() -> None:
    """
    Rensar Terminalen
    """
    command = 'clear'

    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)
