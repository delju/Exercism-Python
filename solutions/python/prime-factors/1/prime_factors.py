"""
Exercice Python: Prime factors
"""

def factors(value):
    """
    Fonction qui renvoie une liste des facteurs premiers d'un nombre 
    """
    prime_factors = []
    divisor = 2 
    "Tant que la valeur est supérieur à 1, on divise par le divisor, si c'est bon, on le stock et on garde la valeur du nombre divisé si non, on augmente de divisor de 1"
    while value > 1: 
        if value % divisor == 0: 
            prime_factors.append(divisor)
            value = value // divisor

        else: 
            divisor += 1

    return prime_factors
