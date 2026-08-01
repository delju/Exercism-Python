"""
Exercice Python: Queen attack
"""

class Queen:
    def __init__(self, row, column):
        """
        Fonction qui initie la reine sur une case
        """
        #Message d'erreur pour la coordonnée de la ligne
        if row < 0:
            raise ValueError("row not positive")
        if row > 7: 
            raise ValueError("row not on board")
        #message d'erreur pour la coordonnée de la colonne
        if column < 0: 
            raise ValueError("column not positive")
        if column > 7: 
            raise ValueError("column not on board")
        #Si c'est bon, on enregistre les valeurs
        self.row = row
        self.column = column

    def can_attack(self, another_queen):
        """
        Fonction pour savoir si les reines peuvent s'attaquer
        """
        #Si elles sont sur la même case, on envoi un message d'erreur
        if self.row == another_queen.row and self.column == another_queen.column: 
            raise ValueError("Invalid queen position: both queens in the same square")

        #Si elles sont sur la même ligne OU la même colonne, revoi Vrai
        if self.row == another_queen.row or self.column == another_queen.column: 
            return True
        #Si elles sont sur la même diagonale, on renvoi Vrai
        if abs(self.row - another_queen.row) == abs(self.column - another_queen.column):
            return True
        #Si non, on renvoi Faux
        return False
            
