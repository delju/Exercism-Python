"""
Exercice Python: Acronym
"""

def abbreviate(words):
    """
    Fonction qui va traduire une phrase en un acronyme 
    """
    #On ajoute chaque première lettre en majuscule des mots nettoyés et séparés
    return "".join(each[0].upper() for each in words.replace("-", " ").replace("_", " ").split())
    
    
