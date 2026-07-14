"""
Exercice Python Matching Brackets
Trouver si chaque accolades ouvertes sont fermées 
"""

def is_paired(input_string):
    stack = []  
    paired = {"]" : "[", "}" : "{", ")" : "("}

    """ Pour chaque élément du texte d'entrée"""
    for caractere in input_string: 
        """Si le caractère est un accolade ouverte, on l'ajoute dans la pile"""
        if caractere in ["[", "{", "("]:
            stack.append(caractere)
            """Si le caractère est dans paired et qu'il n'est pas dans pile ou qu'il ne se retrouve pas dans la liste de paire"""
        elif caractere in paired:
            if not stack or stack.pop() != paired[caractere]: 
                return False
    return len(stack) == 0