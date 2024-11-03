from models import *


class Gear:
    
    
    def __init__(self, name, slot, strength=0, mana=0, hitChance=0) -> None:
        self.name = name
        self.slot = slot
        self.strength = strength
        self.mana = mana
        self.hitChance = hitChance
        
    def equip_item(self, player: Player):
        if self.slot == 'Head':
            player.items['Head'] = self
            player.strength += self.strength
            player.mana += self.mana
            player.hitChance += self.hitChance