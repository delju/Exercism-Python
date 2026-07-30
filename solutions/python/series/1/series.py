"""
Exercice Python: Series
"""

def slices(series, length):
    """
    Fonction qui permet de rédiger une serie de nombre avec la longueur souhaité dans une serie de chiffre donnée
    """

    if length == 0: 
        raise ValueError("slice length cannot be zero")
    if length < 0: 
        raise ValueError("slice length cannot be negative")
    if len(series) == 0: 
        raise ValueError("series cannot be empty")
    if len(series) < length: 
        raise ValueError("slice length cannot be greater than series length")

    results = []
    #On va découper la série, index par index en s'arrêtant lorsqu'il reste le nombre exacte de chiffre qui représente la longueur et on l'ajoute aux résultats en ne gardant que la partie souhaitée
    for index in range(len(series) - length + 1): 
        results.append(series[index:index+length])
    return results