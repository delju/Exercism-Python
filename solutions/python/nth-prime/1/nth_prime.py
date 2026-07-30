"""
Exercice Python: Nth prime
"""

def prime(number):
    """
    Fonction qui permet à trouvé le nombre première à la place demandée 
    """

    if number < 1: 
        raise ValueError('there is no zeroth prime')

    def is_prime(numb): 
        """
        Sous fonction qui vérifie si un nombre est premier ou non
        """
        if numb < 2: 
            return False
            
        last_index = int((numb**0.5) +1)
        
        for each in range(2, last_index): 
            
            if numb % each == 0: 
                return False 
        
        return True

    count = 0
    current_number = 1

    #Tant que le compteur est plus petit que l'ordre demandé on demande si chaque nombre est premier, on ajoute 1 au compteur
    while count < number: 
        current_number += 1
        if is_prime(current_number): 
          count += 1

    return current_number