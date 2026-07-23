"""
Exercice Python: Forth
"""

class StackUnderflowError(Exception):
    pass

def evaluate(input_data):
    stack, custom = [], {}

   # Fonctions nommées locales pour les opérations complexes
    def addition():
        stack.append(stack.pop() + stack.pop())

    def multiplication():
        stack.append(stack.pop() * stack.pop())

    def soustraction():
        b = stack.pop()
        a = stack.pop()
        stack.append(a - b)

    def division():
        b = stack.pop()
        a = stack.pop()
        if b == 0:
            raise ZeroDivisionError("divide by zero")
        stack.append(a // b)

    def dupliquer():
        stack.append(stack[-1])

    def intervertir():
        # En Forth, swap inverse l'ordre des deux derniers éléments
        b = stack.pop()
        a = stack.pop()
        stack.extend([b, a])

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
        if not words: continue

        # 1. Définition de mot personnalisé (: ... ;)
        if words[0] == ":":
            name = words[1]
            if name.isdigit() or (name.startswith("-") and name[1:].isdigit()):
                raise ValueError("illegal operation")
            custom[name] = [w for x in words[2:-1] for w in custom.get(x, [x])]
            continue

               # 2. Remplacement et exécution
        for w in [w for x in words for w in custom.get(x, [x])]:
            if w.isdigit() or (w.startswith("-") and w[1:].isdigit()):
                stack.append(int(w))
            elif w in operations:
                # CORRECTION : On calcule la sécurité dynamiquement pour tout le monde !
                securite = 2 if w in ("+", "-", "*", "/", "swap", "over") else 1
                if len(stack) < securite: 
                    raise StackUnderflowError("Insufficient number of items in stack")
                
                # Sécurité spécifique pour la division par zéro
                if w == "/" and stack[-1] == 0: 
                    raise ZeroDivisionError("divide by zero")
                
                # On exécute la fonction associée
                operations[w]()
            else:
                raise ValueError("undefined operation")


    return stack