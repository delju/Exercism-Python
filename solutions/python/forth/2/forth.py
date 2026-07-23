"""
Exercice Python: Forth
"""

class StackUnderflowError(Exception):
    pass

def evaluate(input_data):
    stack, custom = [], {}

    # Dictionnaire des opérations arithmétiques
    calculs = {
        "+": lambda: stack.append(stack.pop() + stack.pop()),
        "*": lambda: stack.append(stack.pop() * stack.pop()),
        "-": lambda: (b := stack.pop(), a := stack.pop(), stack.append(a - b)),
        "/": lambda: (b := stack.pop(), a := stack.pop(), b == 0 and (_ for _ in ()).throw(ZeroDivisionError("divide by zero")), stack.append(a // b))
    }

    # Dictionnaire des manipulations de pile
    piles = {
        "dup": lambda: stack.append(stack[-1]),
        "drop": lambda: stack.pop(),
        "swap": lambda: stack.extend([stack.pop(), stack.pop()]),
        "over": lambda: stack.append(stack[-2])
    }

    for line in input_data:
        words = line.lower().split()
        if not words: continue

        # 1. Définition de mot personnalisé (: ... ;)
        if words[0] == ":":
            name = words[1]
            if name.isdigit() or (name.startswith('-') and name[1:].isdigit()):
                raise ValueError("illegal operation")
            custom[name] = [w for x in words[2:-1] for w in custom.get(x, [x])]
            continue

        # 2. Remplacement et exécution
        for w in [w for x in words for w in custom.get(x, [x])]:
            if w.isdigit() or (w.startswith('-') and w[1:].isdigit()):
                stack.append(int(w))
            elif w in calculs:
                if len(stack) < 2: raise StackUnderflowError("Insufficient number of items in stack")
                if w == "/" and stack[-1] == 0: raise ZeroDivisionError("divide by zero")
                calculs[w]()
            elif w in piles:
                if len(stack) < (2 if w in ("swap", "over") else 1):
                    raise StackUnderflowError("Insufficient number of items in stack")
                piles[w]()
            else:
                raise ValueError("undefined operation")

    return stack

