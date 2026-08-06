"""
Exercice Python: Matrix
"""

class Matrix:
    """
    Classe qui traduit une chaine de caractère en grille
    """
    def __init__(self, matrix_string):
        self.matrix = [
            [int(number) for number in line.split()]
            for line in matrix_string.split("\n")
        ]

    def row(self, index):
        """
        Fonction qui extrait une ligne sous forme de liste de nombre
        """
        return self.matrix[index - 1]

    def column(self, index):
        """
        Fonction qui extrait une colonne sous forme de liste de nombre
        """
        return [line[index - 1 ] for line in self.matrix]