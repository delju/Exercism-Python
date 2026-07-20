"""
Exercice Python : Eliud's Eggs: Compter le nombre de 1 dans un nombre binaire 
"""

def egg_count(display_value):
    """
    Fonction qui va compter le nombre de 1 dans le nombre binaire pour le convertir en nombre décimal 
    """
    #Initialisation du compteur
    total_egg = 0

    #Tant que le nombre est supérieur à 0
    while display_value > 0:  

        #Si le nombre égal 1, on ajoute 1 au compteur
        if display_value & 1 == 1: 
            total_egg += 1

        #Si c'est 0, on décale vers la droite
        display_value >>= 1 
        
    #On retourne le nombre total d'oeufs
    return total_egg
        
