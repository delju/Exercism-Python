"""
Exercice Python: Dominoes 
"""

def can_chain(dominoes):
    """
    Fonction qui va générer une chaine avec les dominos donnés si possible
    """

    #Si la liste des dominos est vide
    if not dominoes:
        return []
    #Si il n'y a que 1 dominos
    if len(dominoes) == 1:
        #Et que le dominos a deux chiffres identiques
        if dominoes[0][0] == dominoes[0][1]: 
            return dominoes 
        return None
    
    def search(chain, rest): 
        """
        Sous fonction qui va faire la recherche de dominos dans ceux qu'ils restent
        """
        #Si il n'y a plus de reste
        if not rest: 
            #Et que le premier chiffre du premier dominos est égal au dernier chiffre du dernier dominos, on retourne la chaine.
            if chain[0][0] == chain[-1][1]:
                return chain
            return None

        #Cible= dernier chiffre du dernier domino
        target = chain[-1][1]

        #Pour chaque élément du reste, on récupére le dominos et son index 
        for index, domino in enumerate(rest): 
                
            new_rest = rest[:index] + rest[index + 1:]

            # Si le domino s'emboite 
            if domino[0] == target: 
                result = search(chain + [domino], new_rest)
                if result is not None:
                    return result

            #Si le domino s'emboite en étant inversé
            if domino[1] == target: 
                domino_inverse = domino[::-1]
                result = search(chain + [domino_inverse], new_rest)
                if result is not None: 
                    return result

        return None

    # On teste chaque domino de la liste originale comme point de départ
    for index, first_domino in enumerate(dominoes):
        # La réserve contient tous les dominos SAUF celui qu'on a choisi pour démarrer
        initial_rest = dominoes[:index] + dominoes[index+1:]

        # Essai A : On commence avec le premier domino à l'endroit
        result = search([first_domino], initial_rest)
        if result is not None:
            return result

        # Essai B : On commence avec le premier domino à l'envers
        result = search([first_domino[::-1]], initial_rest)
        if result is not None:
            return result

    # Si après avoir testé TOUS les points de départ, aucun n'a marché : c'est impossible !
    return None

        
        
