
directory = {
    1: "a",
    2: "b",
    3: "c",
    4: "d",
    5: "e",
    6: "f",
    7: "c",
    8: "h",
    9: "i",
}

print(f'dictionary(Values):{directory.values()}')
print(f'dictionary(Items):{directory.items()}')

for (key, value) in directory.items():
    print(f'Item {key}:{value}')
