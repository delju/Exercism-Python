"""
Exercice Python: Forth
"""

class StackUnderflowError(Exception):
    pass


def evaluate(input_data):
    """
    Évalue une liste d'instructions Forth et renvoie l'état final de la pile.
    """
    stack = []
    custom_word = {}

    for line in input_data:
        # On découpe la ligne en minuscules
        words = line.lower().split()
        
        if not words:
            continue

        # 1. CAS A : L'utilisateur définit un nouveau mot personnalisé
        if words[0] == ":":
            name = words[1]
            # Sécurité : impossible de redéfinir un nombre !
            if name.isdigit() or (name.startswith('-') and name[1:].isdigit()):
                raise ValueError("illegal operation")
                
            # On extrait la définition (tout ce qui est entre le nom et le ';')
            definition = words[2:-1]
            
            # Étape magique : si la définition utilise un mot personnalisé déjà connu,
            # on remplace ce mot par sa valeur actuelle pour éviter les boucles infinies.
            expanded_def = []
            for w in definition:
                if w in custom_word:
                    expanded_def.extend(custom_word[w])
                else:
                    expanded_def.append(w)
                    
            custom_word[name] = expanded_def
            continue

        # 2. CAS B : On exécute une ligne normale. 
        # On remplace d'abord les mots personnalisés par leur définition.
        instructions = []
        for w in words:
            if w in custom_word:
                instructions.extend(custom_word[w])
            else:
                instructions.append(w)

        # 3. On lit et exécute chaque instruction de gauche à droite
        for word in instructions:
            if word.isdigit() or (word.startswith('-') and word[1:].isdigit()):
                stack.append(int(word))
                
            elif word == "+":
                if len(stack) < 2: raise StackUnderflowError("Insufficient number of items in stack")
                stack.append(stack.pop() + stack.pop())
                
            elif word == "-":
                if len(stack) < 2: raise StackUnderflowError("Insufficient number of items in stack")
                operator_2 = stack.pop()
                operator_1 = stack.pop()
                stack.append(operator_1 - operator_2)
                
            elif word == "*":
                if len(stack) < 2: raise StackUnderflowError("Insufficient number of items in stack")
                stack.append(stack.pop() * stack.pop())
                
            elif word == "/":
                if len(stack) < 2: raise StackUnderflowError("Insufficient number of items in stack")
                operator_2 = stack.pop()
                operator_1 = stack.pop()
                if operator_2 == 0:
                    raise ZeroDivisionError("divide by zero")
                stack.append(operator_1 // operator_2)
                
            elif word == "dup":
                if len(stack) < 1: raise StackUnderflowError("Insufficient number of items in stack")
                stack.append(stack[-1])
                
            elif word == "drop":
                if len(stack) < 1: raise StackUnderflowError("Insufficient number of items in stack")
                stack.pop()
                
            elif word == "swap":
                if len(stack) < 2: raise StackUnderflowError("Insufficient number of items in stack")
                operator_2 = stack.pop()
                operator_1 = stack.pop()
                stack.append(operator_2)
                stack.append(operator_1)
                
            elif word == "over":
                if len(stack) < 2: raise StackUnderflowError("Insufficient number of items in stack")
                stack.append(stack[-2])
                
            else:
                # Si le mot n'est ni un nombre ni une opération connue
                raise ValueError("undefined operation")

    return stack
