def rotate(text, key):

    #Initier résultat
    resultat = ""

    #Boucle pour chaque élément du text, le déplacer selon la clé
    for caractere in text: 

        #Si la lettre est une majuscule, on garde une majuscule, méthode ASCII départ 65
        if caractere.isupper(): 
            new_code = ((ord(caractere) - 65 + key) % 26) + 65
            new_letter = chr(new_code)
            resultat += new_letter

        #Si la lettre est une minuscule, on garde une minuscule, méthode ASCII départ 97
        elif caractere.islower():
            new_code = ((ord(caractere) - 97 + key) % 26) + 97
            new_letter = chr(new_code)
            resultat += new_letter
        
        #Si c'est un espace, une ponctuation, on le laisse telquel
        else: 
            resultat += caractere

    return resultat
