""" Module de résolution de l'exercice Pig Latin pour Exercism."""

def translate(text):
    #Diviser la phrase à chaque espace pour n'avoir que les mots
    mots = text.split()
    #On Initie la variable pour les voyelles en anglais
    voyelles = "aeiou"
    #Initié la variable pour les mots traduits
    mots_traduit = []

    #Boucle pour chaque mot, on va traduire en pig latin
    for mot in mots:
    #1er REGLE: Si le mot commence par une voyelle ou par xr ou yt, on ajoute simplement ay à la fin du mot
        if mot[0] in voyelles or mot.startswith(("xr" , "yt")):
            return mot + "ay"
            break

        #Pour la suite, il faut découper le mot, donc il faut d'abord déterminer le point de rupture 
        index_coupure = 0 

        #Boucle: pour chaque lettre du mot, on va déterminer l'index et la lettre associée.
        for index, letter in enumerate(mot): 
        
            #Régle 4
            #Si la lettre est y, mais qu'elle ne commence pas par celle ci, on donne l'index de la lettre
            if letter == "y" and index > 0: 
                index_coupure = index
                #On arrête la boucle car on a trouvé le point de rupture 
                break

            #Régle 3
            #Il faut trouver 'qu' donc un 'u' précédé d'un 'q'
            if letter == "u" and mot[index-1] == 'q': 
                index_coupure = index+1 
                break 

            #Régle 3 
            #Dès la première voyelle 
            if letter in voyelles: 
                index_coupure = index
                break

        #Maintenant on va effectuer la rupture du mot
        debut_mot = mot[:index_coupure]
        fin_mot = mot[index_coupure:]
        mots_traduit.append(fin_mot + debut_mot + "ay")

    return " ".join(mots_traduit)

        
    