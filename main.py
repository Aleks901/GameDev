from models import *
from time import sleep

player = Player(None, 10, 10, 10, 10)
gloves = Gear("helm", "Head")
player.inventory.append(gloves)


def menu_loop():
    running = True
    while running:
        print("Main Menu:")
        print("______________")
        print("1. Inventory")
        print("2. Adventure")
        check_answer = input("Choose an option: ")
        if check_answer == "1":
            inventory_loop()
            break
        elif check_answer == "2":
            print("That hasn't been added yet")
            break
        else:
            print("Error: Wrong input")
        
def inventory_loop():
    running = True
    while running:
        print("___________________")
        print("Inventory:")
        print(list(enumerate(player.inventory)))
        print("1. Equip item")
        print("2. Unequip item")
        print("3. Check equiped gear")
        print("4. Exit inventory")
        check = input("Choose an option: ")
        if check == "1":
            wanted_item = int(input("Which item would you like to equip?: "))
            Gear.equip_item(player.inventory[wanted_item], player)
            player.inventory.pop(wanted_item)
        elif check == "2":
            unwanted_item = input("Which item would you like to unequip?: ")
            
        
        elif check == "3":
            print("_________________")
            print("Equipped items:")
            print(player.items)   
            print("_________________") 
            
        elif check == "4":
            break
        else:
            print("Error: Invalid option!")
            

if __name__ == "__main__":
    menu_loop()
            
        
