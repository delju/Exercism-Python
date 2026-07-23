"""
Exercice Python: Forth
"""

class StackUnderflowError(Exception):
    """Exception levée lorsque la pile ne contient pas assez d'éléments."""
    pass


def evaluate(input_data):
    """
    Évalue une liste d'instructions Forth et renvoie l'état final de la pile.
    """
    stack, custom = [], {}

    # Fonctions nommées locales pour les opérations complexes
    def addition():
        stack.append(stack.pop() + stack.pop())

    def multiplication():
        stack.append(stack.pop() * stack.pop())

    def soustraction():
        last_value = stack.pop()
        previous_value = stack.pop()
        stack.append(previous_value - last_value)

    def division():
        divisor = stack.pop()
        dividend = stack.pop()
        if divisor == 0:
            raise ZeroDivisionError("divide by zero")
        stack.append(dividend // divisor)

    def dupliquer():
        stack.append(stack[-1])

    def intervertir():
        last_value = stack.pop()
        previous_value = stack.pop()
        stack.extend([last_value, previous_value])

    def copier_deuxieme():
        stack.append(stack[-2])

    # Dictionnaire d'aiguillage propre associant les mots à de vraies fonctions
    operations = {
        "+": addition, 
        "*": multiplication, 
        "-": soustraction, 
        "/": division,
        "dup": dupliquer, 
        "drop": stack.pop, 
        "swap": intervertir, 
        "over": copier_deuxieme
    }
    
    for line in input_data:
        words = line.lower().split()
        if not words: 
            continue

        # 1. Définition de mot personnalisé (: ... ;)
        if words[0] == ":":
            name = words[1]
            if name.isdigit() or (name.startswith("-") and name[1:].isdigit()):
                raise ValueError("illegal operation")
            
            # Étalement propre de la définition pour la lisibilité
            expanded_def = []
            for raw_word in words[2:-1]:
                expanded_def.extend(custom.get(raw_word, [raw_word]))
            custom[name] = expanded_def
            continue

        # 2. Remplacement et création de la liste d'instructions
        instructions = []
        for raw_word in words:
            instructions.extend(custom.get(raw_word, [raw_word]))

        # 3. Exécution en cascade épurée des variables d'une lettre
        for instruction in instructions:
            if instruction.isdigit() or (instruction.startswith("-") and instruction[1:].isdigit()):
                stack.append(int(instruction))
                
            elif instruction in operations:
                # CORRECTION R6201 : Utilisation d'un ensemble {} pour le test d'appartenance
                if instruction in {"+", "-", "*", "/", "swap", "over"}:
                    securite = 2
                else:
                    securite = 1
                    
                if len(stack) < securite: 
                    raise StackUnderflowError("Insufficient number of items in stack")
                if instruction == "/" and stack[-1] == 0: 
                    raise ZeroDivisionError("divide by zero")
                operations[instruction]()
                
            else:
                raise ValueError("undefined operation")

    return stack

