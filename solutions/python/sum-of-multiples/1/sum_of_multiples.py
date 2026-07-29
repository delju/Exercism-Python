"""
Exercice Python: Sum of multiples 
"""

def sum_of_multiples(limit, multiples):
    """
    Fonction qui va récupérer les mutliples des nombres dans la liste jusqu'à la limite, puis enlever les doublons et additionner tout ces multiples
    """
    #Variable set (il va supprimer automatiquement les doublons)
    result = set() 
    #Boucle pour parcourir tout les nombres de multiples
    for number in multiples: 
        #Si c'est égale à 0 on continue
        if number == 0: 
            continue
        #On met à jour le set avec les mutliples de chaque nombre
        result.update(range(number, limit, number))
    #On retourne la somme de ces nombres
    return sum(result)
