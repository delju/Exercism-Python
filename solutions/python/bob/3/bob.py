def response(hey_bob):
    """
    Nettoyé la phrase pour enlever tout les espaces blancs et éviter les erreurs.

    Si la phrase est vide = "Fine. Be that way!"
    Si la phrase est crier et interrogative = "Calm down, I know what I'm doing!"
    Si la phrase est seulement interrogative = "Sure."
    Si la phrase est crier = "Whoa, chill out!"
    Pour toutes autres phrases = "Whatever."
    """
    hey_bob = hey_bob.strip()
    
    if hey_bob == "": 
        say = "Fine. Be that way!"

    elif hey_bob.isupper() and hey_bob.endswith("?"):
        say = "Calm down, I know what I'm doing!"
        
    elif hey_bob.endswith("?"): 
        say = "Sure."

    elif hey_bob.isupper(): 
        say = "Whoa, chill out!"

    else: 
        say = "Whatever."

    return say