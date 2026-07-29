"""
Exercice Python: List OPS
"""

def append(list1, list2):
    """
    Fonction qui permet de générer un append
    """
    new_list = [] + list1
    for element in list2: 
        new_list = new_list + [element]

    return new_list

def concat(lists):
    """
    Fonction qui permet d'applatir une liste sans la méthode native
    """
    new_list = [] 
    for sublist in lists:
        # On appelle la fonction append que vous avez créée plus haut
        new_list = append(new_list, sublist)

    return new_list


def filter(function, list):
    """
    Fonction qui filtre la liste en fonction de la demande et renvoie une liste des éléments qui passent le filtre
    """
    result = []
    for element in list: 
        if function(element): 
            result = result + [element]
    return result


def length(list):
    """
    Fonction qui renvoie le nombre total d'element dans une liste
    """
    count = 0 
    for element in list: 
        count = count + 1

    return count


def map(function, list):
    """
    Fonction qui transforme les éléments d'une liste et renvoie la liste transformée
    """
    new_list = []
    for element in list: 
        new_element = function(element)
        new_list = new_list + [new_element]
    return new_list
    


def foldl(function, list, initial):
    
    accumulator = initial
    for element in list: 
        accumulator = function(accumulator, element)
    return accumulator


def foldr(function, list, initial):
    
    reversed_list = [] 
    accumulator = initial
    
    for element in list: 
        reversed_list = [element] + reversed_list
        
    for each in reversed_list: 
        accumulator = function(accumulator, each)
    return accumulator

        


def reverse(list):
    """
    Fonction qui renvoie la liste inversée
    """
    reversed_list = [] 
    for element in list: 
        reversed_list = [element] + reversed_list
        
    return reversed_list
 