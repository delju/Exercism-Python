"""
Exercice Python: Flatten array
"""

def flatten(iterable):
    """
    Fonction qui va applatir une liste imbriquée en excluant les nones
    """
    result = [] 
    #Boucle pour parcourir chaque élément afin de l'ajouter à une nouvelle liste
    for element in iterable: 
        #Si cet élément est une liste, il faut la déballer la sous liste, on utilise la méthode récurisive en rappelant la fonction flatten sur les éléments et l'ajoute déballée avec extend.
        if isinstance(element, list): 
            result.extend(flatten(element))
        #Et si l'élément n'est pas none, on l'ajoute
        elif element is not None: 
            result.append(element)

    return result
    