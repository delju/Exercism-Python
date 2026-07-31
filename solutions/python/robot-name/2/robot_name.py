"""
Exercice Python: Robot name
"""
import random

class Robot:
    """
    Classe représentant un robot
    """
    def __init__(self):
        self.name = None
        self.reset()

    used_name = set()

    def reset(self): 
        """
        Fonction qui va donner un nom au robot aléatoirement lorsqu'il nait ou reset
        """
        while True:
            #On détermine aléatoirement les deux lettres et les nombres
            letter_1 = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
            letter_2 = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

            numbers = random.randint(100, 999)
            #On assemble le tout
            potential_name = f"{letter_1}{letter_2}{numbers}"
            #Si le nom potentiel n'est pas encore utiliser, on l'ajoute à la liste (pour ne pas être utiliser plus tard), on donne ce nom au robot et on arrête la boucle
            if potential_name not in Robot.used_name: 
                Robot.used_name.add(potential_name)

                self.name = potential_name

                break