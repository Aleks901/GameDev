from models import *

class Player:
    
    
    def __init__(self, 
                 name: str, 
                 health:int, 
                 mana:int, 
                 energy:int,
                 hitChance = 0) -> None:
        """The player class controls all the basic functionalities and modifiers of
        the player itself in the game

        Args:
            name (str): The player's name
            health (int): The player's health
            mana (int): The player's mana
            energy (int): The player's energy
            hitChance (int): hitChance modifies the palyer's true damage

        Vars:
            attackpower (int): Attack power is the player's true damage
            strength (int): Strength modifies the player's true damage and adds to it
        """
        self.name = name
        self.health = health
        self.mana = mana
        self.energy = energy
        self.hitChance = hitChance
        self.level = 1
        self.attack_power = 10 + (self.level*2)
        self.strength = 5 + (self.level*2)
        self.accuracy = 10 + (self.level*2)
        self.items = {'Head': None, 'Chest': None, 'Legs': None, 'Weapon': None}
        self.inventory = []
        
        
    def calculate_hit_chance(self, selected_target: Enemy):
        hitchance = self.hitChance + (self.accuracy / (self.accuracy + selected_target.evasion)) * 100
        return hitchance
        
    def attack(self, target: Enemy):
        hit_chance = self.calculate_hit_chance(target)
        damage = (self.attack_power + self.strength/2) + (hit_chance/10)
        if hit_chance >= 30:
            target.health -= damage
        else:
            damage = 0
            print("Your attack missed!")
        print(f"Your hitchance: {hit_chance}%") # Used for testing
        print(f"You hit your target for: {damage} Damage!") # Used for testing
    
    
            