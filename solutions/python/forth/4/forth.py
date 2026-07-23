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
        """addition des éléments"""
        stack.append(stack.pop() + stack.pop())

    def multiplication():
        """Mutliplication des éléments"""
        stack.append(stack.pop() * stack.pop())

    def soustraction():
        """Soustraction des éléments"""
        last_value = stack.pop()
        previous_value = stack.pop()
        stack.append(previous_value - last_value)

    def division():
        """Division des éléments, attention, si le diviseur est 0, on revoie une erreur"""
        divisor = stack.pop()
        dividend = stack.pop()
        if divisor == 0:
            raise ZeroDivisionError("divide by zero")
        stack.append(dividend // divisor)

    def dupliquer():
        """fonction DUP"""
        stack.append(stack[-1])

    def intervertir():
        """Fonction SWAP"""
        # CORRECTION C0104 : Remplacement de 'b' et 'a' par des noms explicites
        last_value = stack.pop()
        previous_value = stack.pop()
        stack.extend([last_value, previous_value])

    def copier_deuxieme():
        """Fonction OVER"""
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
            custom[name] = [w for x in words[2:-1] for w in custom.get(x, [x])]
            continue

        # 2. Remplacement et exécution
        for instruction in [instruction for raw_word in words for instruction in custom.get(raw_word, [raw_word])]:
            if instruction.isdigit() or (instruction.startswith("-") and instruction[1:].isdigit()):
                stack.append(int(instruction))
            elif instruction in operations:
                securite = 2 if instruction in ("+", "-", "*", "/", "swap", "over") else 1
                if len(stack) < securite: 
                    raise StackUnderflowError("Insufficient number of items in stack")
                if instruction == "/" and stack[-1] == 0: 
                    raise ZeroDivisionError("divide by zero")
                operations[instruction]()
            else:
                raise ValueError("undefined operation")

    return stack
