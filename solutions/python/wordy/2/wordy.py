def answer(question):
    """
    Parse et calcule une question mathématique textuelle de gauche à droite.
    """
    if not question.startswith("What is"):
        raise ValueError("unknown operation")
        
    # Nettoyage de la chaîne
    question = question.removeprefix("What is").removesuffix("?").strip() 
    question = question.replace("multiplied by", "multiplied").replace("divided by", "divided")

    tokens = question.split()

    if not tokens:
        raise ValueError("syntax error")

    # Sécurité 1 : Le premier élément doit obligatoirement être un nombre
    try:
        total = int(tokens[0])
    except ValueError as erreur:
        raise ValueError("syntax error") from erreur

    index = 1  
    while index < len(tokens):
        operation = tokens[index]
        
        # Sécurité 2 : L'opération existe-t-elle ?
        if operation not in ["plus", "minus", "multiplied", "divided"]:
            est_un_nombre = False
            try:
                int(operation)
                est_un_nombre = True
            except ValueError:
                est_un_nombre = False

            # Si c'est un nombre et non une opération
            if est_un_nombre:
                raise ValueError("syntax error")
            raise ValueError("unknown operation")
            
        # Sécurité 3 : Le terme suivant est-il bien un nombre ?
        try:
            prochain_nombre = int(tokens[index + 1])
        except (ValueError, IndexError) as erreur:
            raise ValueError("syntax error") from erreur
            
        # Application du calcul
        if operation == "plus":
            total += prochain_nombre
        elif operation == "minus":
            total -= prochain_nombre
        elif operation == "multiplied":
            total *= prochain_nombre
        elif operation == "divided":
            total //= prochain_nombre
            
        index += 2

    return total
