
menu_in_funktion = True
menu_option = ["1", "2", "3"]  # * Vilka meny options osm användaren kan välja

while menu_in_funktion:
    userawnser = ""
    while userawnser not in menu_option:
        userawnser = input("""
==============================================
                  MAIN MENU
==============================================
  1. PLAY GAME        | Type:  1
  2. HOW TO PLAY      | Type:  2
  3. QUIT             | Type:  3
==============================================
TYPE: """)
        match userawnser:  # * Vilken varaibel man kollar igenom

            case "1":  # * Filter 1
                print(1)

            case "2":  # * Filter 2
                print(2)

            case "3":  # * Filter 3
                print(3)

            case __:  # * Resten
                print("number")
