"""
Exercice Python: Proverb
"""

def proverb(*items, qualifier):
    """
    Générer un proverbe selon les éléments donnés
    """
    if not items:
        return []
        
    result = []

    #Pour chaque premier et second élément des couples de mots des items, on ajoute une phrase
    for first_item, second_item in zip(items, items[1:]):
        result.append(f"For want of a {first_item} the {second_item} was lost.")
    #Pour le qualifier, si il est none on ne met rien, si il est spécifié on l'ajoute à la dernière phrase.
    if qualifier is None: 
        result.append(f"And all for the want of a {items[0]}.")
    else: 
        result.append(f"And all for the want of a {qualifier} {items[0]}.")

    return result