from models import *

test_player = Player("Player", 10, 10, 10)
test_enemy = Enemy("Test", 10, 10, 10, 10)
test_item = Gear("Flaming Head of power", 'Head', hitChance=0, strength=0)


test_item.equip_item(test_player)
print(test_player.items)



test_player.attack(test_enemy)
test_player.attack(test_enemy)
test_player.attack(test_enemy)
test_player.attack(test_enemy)

"""print(test_enemy.health)
print(test_player.attack_power)"""