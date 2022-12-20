from time import sleep

from rich import inspect
from rich.progress import track

menu_options = ["1", "2", "3", "game", "how to play" "quit"]

ORG_Awnser = input("Type ")

# for i in range(len(menu_options)):
#     if ORG_Awnser == menu_options[i]:
#         if ORG_Awnser.isalpha():
#             print(ORG_Awnser.lower())
#         else:
#             print(ORG_Awnser)


#     else:
#         # funk_Clearterminal()
#         print("You passed in the wrong type of Awnsers")
#         for i in track(range(5)):
#             sleep(1)
#         break
# print("NONE")


if ORG_Awnser not in menu_options:
    print("JA")

if ORG_Awnser in menu_options:
    print("NEJ")
