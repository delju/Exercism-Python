"""
Exercice python: Square root 
"""

def square_root(number):
    """
    Fonction qui recherche la racine carrée d'un nombre
    """
    square = 1
    #On teste tout les nombres jusqu'à trouver le bon, en mutlipliant le nombre par lui même.
    while square * square <= number: 
        if square * square == number:
            return square

        square += 1