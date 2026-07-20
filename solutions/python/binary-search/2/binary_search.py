"""
Exercice Python: Binary search
Retrouver la position du nombre dans une liste donné et triée 
"""

def find(search_list, value):
    """
    Fonction permettant de trouver le chiffre demandé. 
    Pour ce faire, nous diviser en deux et garder la partie où pourrait se trouver le chiffre demandé, jusqu'à la réduction complète de la liste 
    """

    #Valeur du début de la liste
    left_value = 0 

    #Valeur de la fin de la liste 
    right_value = len(search_list) - 1

    #Boucle, tant que la valeur de gauche est inférieur ou égale à la valeur de droite. 
    while left_value <= right_value:

    #Nous cherchons la valeur du milieu 
        middle_value = (left_value + right_value) // 2

        #Les trois scénarios possible. 1.Si la valeur recherchée est égale à celle du milieu de la liste 
        if search_list[middle_value] == value: 
            return middle_value

        #2. Si la valeur du milieu est plus grand que la valeur rechercher, on déplace le curseur de la valeur de droite à la valeur du milieu - 1
        if search_list[middle_value] > value: 
            right_value = middle_value - 1
        
        #Si la valeur du milieur est plus petit que la valeur rechercher, on déplace le curseur de la valeur de gauche, à la valeur du milieu + 1
        else: 
            left_value = middle_value + 1

    #Et si la valeur n'est pas trouvée, alors c'est qu'elle n'existe pas dans la liste et nous renvoyons une erreur
    raise ValueError("value not in array")
