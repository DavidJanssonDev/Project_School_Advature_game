import random

from game_classes import Player
from terminal_fixes import clearterminal


def tap_calc(rund_effect: float, player: Player, effect_type: str):
    """

    Calculates the damage and the turns the debuff effect last

    Returns:
        int:
    """

    d_buff_time: int = random.randint(1, 2) + player.p_turn
    d_buff_temp: int = (pow(player.p_turn, rund_effect) + 0.5)/100
    d_buff: float = round(1-d_buff_temp, 3)

    return [effect_type, d_buff, d_buff_time]


def de_buff_check(player: Player) -> None:
    """

    Summery:

        Checks if the user d-buffs has run out

    Parameter:

        player (Player): User player
    """
    curret_turn: int = player.p_turn
    debuffs: list[list] = player.player_debuff

    for index, numberlist in enumerate(debuffs):
        if numberlist[2] == curret_turn:
            debuffs.pop(index)


def trap_display(random_deffect: str) -> None:
    """
    Display of the trap
    """
    clearterminal()
    input(f"""
==============================================
      !!!!            TRAP             !!!
==============================================

    YOU GOT A TRAP OF TYPE {random_deffect} 


==============================================
            PRESS ENTER TO GET BACK
==============================================
  """)


def trap(player: Player) -> None:
    """
    Funktion för det som händer när man har hamnat i en fälla.


    [['vad för debuff', effect, end rundda], ['vad för debuff', effect, end rundda], ['vad för debuff', effect, end rundda]]


    Args:
        player (Player): spelare klass
    """
    effect: list = []
    random_deffect: str = random.choice(['health', 'damage', 'armor'])
    rund_effect: float
    current_d_buffs: list[list] = player.player_debuff

    match random_deffect:

        case 'health':
            rund_effect: float = 1.388
            effect = tap_calc(rund_effect, player, random_deffect)
        case 'armor':
            rund_effect: float = 1.0682
            effect = tap_calc(rund_effect, player, random_deffect)

        case 'damage':
            rund_effect: float = 1.6245
            effect = tap_calc(rund_effect, player, random_deffect)

    current_d_buffs.append(effect)
    trap_display(random_deffect)
