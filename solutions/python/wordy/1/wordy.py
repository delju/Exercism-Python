def answer(question):

    if not question.startswith("What is"):
        raise ValueError("unknown operation")
        
    #On retire what is des questions
    question = question.removeprefix("What is")

    #On retire les points d'interrogations
    question = question.removesuffix("?")
    
    # Enlève les espaces inutiles autour
    question = question.strip() 

    # "multiplied by" devient juste "multiplied"
    question = question.replace("multiplied by", "multiplied")

    # "divided by" devient juste "divided"
    question = question.replace("divided by", "divided")

    # Transformer la question en liste
    tokens = question.split()

    if not tokens:
        raise ValueError("syntax error")

       # Sécurité : Le premier élément doit obligatoirement être un nombre
    try:
        total = int(tokens[0])
    except ValueError:
        raise ValueError("syntax error")

    i = 1
    while i < len(tokens):
        operation = tokens[i]
        
        # Sécurité 1 : L'opération existe-t-elle ?
        if operation not in ["plus", "minus", "multiplied", "divided"]:
            est_un_nombre = False
            try:
                int(operation)
                est_un_nombre = True  # La conversion a réussi sans planter
            except ValueError:
                est_un_nombre = False # Ce n'est pas un nombre (ex: "cubed")

            # Maintenant on prend la décision en dehors du bloc try/except
            if est_un_nombre:
                raise ValueError("syntax error")
            else:
                raise ValueError("unknown operation")


            
        # Sécurité 2 : Le terme suivant est-il bien un nombre ?
        try:
            prochain_nombre = int(tokens[i + 1])
        except (ValueError, IndexError):
            raise ValueError("syntax error")
            
        # Si tout est OK, on fait le calcul
        if operation == "plus":
            total += prochain_nombre
        elif operation == "minus":
            total -= prochain_nombre
        elif operation == "multiplied":
            total *= prochain_nombre
        elif operation == "divided":
            total //= prochain_nombre  # Division entière pour rester sur des int
            
        i += 2

    return total
