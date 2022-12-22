
class Player(object):

    def __init__(self) -> None:
        self.name = "Bob"
        self.health = 100
        self.damage = 100
        self.armor = 100


class Monster(object):
    def __init__(self) -> None:
        self.name = "Kai"
        self.health = 100
        self.damage = 100
        self.armor = 100


player = Player()
monster = Monster()

userInput = input(f"""

==============================================================
  Player: {player.name}             |     Monster: {monster.name}
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
  Health: {player.health}             |     Health: {monster.health}
  Damage: {player.damage}             |     Damage: {monster.damage}
  Armor: {player.armor}              |     Armor: {monster.armor}
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
 OPTION 1: FIGHT                                    | TYPE: 1
 OPTION 2: USE ITEM [DOSENT USE A TURN]             | TYPE: 2
 OPTION 3: RUN AWAY [LOSE A LIFE AND SIKP BATTEL]   | TYPE: 3
==============================================================
    """)
