"""
Exercice Python: Hamming
"""

def distance(strand_a, strand_b):
    """
    Fonction qui permet de déterminer le nombre de différence entre deux brins d'ADN de la même longueur
    """
    count = 0 

    if len(strand_a) != len(strand_b): 
        raise ValueError("Strands must be of equal length.")

    for letter_a, letter_b in zip(strand_a, strand_b): 
        if letter_a != letter_b: 
            count += 1

    return count
