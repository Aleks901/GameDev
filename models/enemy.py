from models import *

class Enemy:
    
    
    def __init__(self, name, health, mana, energy, evasion=0) -> None:
        self.name = name
        self.health = health
        self.mana = mana
        self.energy = energy
        self.evasion = evasion
        