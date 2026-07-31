"""
Exercice Python: D&D character
"""
import random

class Character:
    """
    Classe d'un personnage avec chaque compétence réparti aléatoirement
    """
    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = 10 + modifier(self.constitution)
        
    def ability(self):
        """
        Fonction qui va calculer aléatoirement les points d'une compétence
        """

        rolls =[random.randint(1,6) for _ in range(4)]
        three_numbers = sorted(rolls)[1:]
    
        return sum(three_numbers)
    

def modifier(value):
    """
    Fonction qui va calculer les points de vie
    """
    return (value - 10) // 2

