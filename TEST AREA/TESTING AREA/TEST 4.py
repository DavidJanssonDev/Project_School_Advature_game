

def funk_inspect_and_lookthrow_items(inventory):
    print(inventory)
    inventoryKeys = [key for key in inventory]
    inventory_Menu_Is_Running = True
    inventory_Menu_options = inventoryKeys + ["quit"]

    while inventory_Menu_Is_Running:
        userawnser = ""
        while userawnser not in inventory_Menu_options:
            print(f"""
==============================================
                Inventory MENU
==============================================

______________________________________________""")
            for key in inventory:
                print(key, ' : ', inventory[key])
            userawnser = input("""
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾

==============================================                    
                               
==============================================                    
Type: """)


inventory = {
    "Item 1": None,
    "Item 2": None,
    "Item 3": None,
    "Item 4": None,
    "Item 5": None,
}

funk_inspect_and_lookthrow_items(inventory)
