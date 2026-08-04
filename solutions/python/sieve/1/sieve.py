"""
Exercice Python: Sieve
"""

def primes(limit):
    """
    Fonction qui renvoie une liste des nombres premiers jusqu'à une limite donnée
    """
    #Si la limite est inférieur à 2, on renvoie une liste vide
    if limit < 2: 
        return []

    #création d'un dictionnaire ou chaque nombre de 2 jusqu'à la limite sont non marqués
    crible = {number : True for number in range(2, limit + 1)}

    #Boucle qui parcourt chaque chiffre jusqu'à la limite et qui marque les multiples du nombres
    for num, tag in crible.items(): 
        if tag: 
            for each in range(num * 2, limit + 1, num):
                crible[each] = False
    #Renvoie la liste des éléments non marqués
    return [number for number, tag in crible.items() if tag]
                
    
