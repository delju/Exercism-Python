def rotate(text, key):

    #Initier résultat
    resultat = ""

    #Boucle pour chaque élément du text, le déplacer selon la clé
    for caractere in text: 
        if caractere.isupper(): 
            new_code = ((ord(caractere) - 65 + key) % 26) + 65
            new_letter = chr(new_code)
            resultat += new_letter

        elif caractere.islower():
            new_code = ((ord(caractere) - 97 + key) % 26) + 97
            new_letter = chr(new_code)
            resultat += new_letter

        else: 
            resultat += caractere

    return resultat
