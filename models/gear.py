from models import *


class Gear:
    
    
    def __init__(self, name, slot, strength=0, mana=0, hitChance=0, evasion=0, energy=0) -> None:
        self.name = name
        self.slot = slot
        self.strength = strength
        self.mana = mana
        self.hitChance = hitChance
        self.evasion = evasion
        self.energy = energy
        
    def __str__(self) -> str:
        return f"{self.name}"
    
    def __repr__(self):
        return self.__str__()
        
    def equip_item(self, player: Player):
        if self.slot == 'Head':
            player.items['Head'] = self
            player.strength += self.strength
            player.mana += self.mana
            player.hitChance += self.hitChance
            
    
    def equip_item_enemy(self, enemy: Enemy):
        if self.slot == 'Head':
            enemy.items['Head'] = self
            enemy.strength += self.strength
            enemy.mana += self.mana
            enemy.evasion += self.evasion
            enemy.energy += self.energy
    
    def unequip_item(self, player: Player):
        if self.slot == 'Head':
            player.inventory.append(self)
            player.items.update({'Head': None})
            player.strength -= self.strength
            player.mana -= self.mana
            player.hitChance -= self.hitChance
            
    