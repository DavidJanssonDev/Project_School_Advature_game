import random

antal = 5

tabbel = []
for runda in range(antal):
    random_number: float = random.random()

    number_1: float = 1/3
    number_2: float = 2/3
    number_3: float = 3/3

    disctance_randnum_num1: float = abs(random_number - number_1)
    disctance_randnum_num2: float = abs(random_number - number_2)
    disctance_randnum_num3: float = abs(random_number - number_3)

    # print(f"{disctance_randnum_num1:5f}")
    # print(f"{disctance_randnum_num2:5f}")
    # print(f"{disctance_randnum_num3:5f}")
    # print(f"{random_number:5f}")

    longest_0 = disctance_randnum_num1 > disctance_randnum_num2 and disctance_randnum_num1 > disctance_randnum_num3
    longest_05 = disctance_randnum_num2 > disctance_randnum_num1 and disctance_randnum_num2 > disctance_randnum_num3
    longest_1 = disctance_randnum_num3 > disctance_randnum_num1 and disctance_randnum_num3 > disctance_randnum_num2

    # print(longest_0)
    # print(longest_05)
    # print(longest_1)

    value = (f"runda {runda}",
             ("num1", 0, f"{disctance_randnum_num1:2f}"),
             ("num2", 0.2, f"{disctance_randnum_num2:5f}"),
             ("num3", 1, f"{disctance_randnum_num3:2f}")
             )
    tabbel.append(value)

print(tabbel)
