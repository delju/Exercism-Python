"""
Exercice Python: Run length encoding
"""

def decode(string):
    """
    Fonction qui décompressé une séquence de chiffres et de lettres, en une séquence de lettres.
    """
    current_count = ""
    decoded_parts = []
    #Pour chaque lettre de la séquence donnée
    for char in string: 
        #Si c'est un chiffre, on l'ajoute dans current_count
        if char.isdigit(): 
            current_count += char
        #Si non, c'est que c'est un lettre ou un espace
        else: 
            #Si current_count n'est pas vide, on mutliplie la lettre par le nombre de current_count
            if current_count: 
                decoded_parts.append((char * int(current_count)))
            #Si non, on ne met que la lettre
            else: 
                decoded_parts.append(char)
            #On réitinialise le compteur
            current_count = ""

    return "".join(decoded_parts)

def encode(string):
    """
    Fonction qui va compresser la séquence de lettres en séquence de chiffre et de lettres
    """
    if not string: 
        return ""

    encoded_parts = []
    current_char = string[0]
    count = 1
    #On faut une boucle à partir de la deuxième lettre
    for char in string[1:]: 
        #Si elle est égale à la lettre précédente, on ajoute 1 au compteur
        if char == current_char: 
            count += 1
        #Si non, si le compteur est plus grand que 1, on ajoute, le compte et la lettre associé
        else: 
            if count > 1: 
                encoded_parts.append(f"{count}{current_char}")
            #Si le compteur est égale à un, on ajoute juste la lettre
            else: 
                encoded_parts.append(current_char)
            #On réinitialise la lettre et le compteur
            current_char = char 
            count = 1
    #Quand la boucle est terminée, il faut ajouter le dernier bloque 
    if count > 1:
        encoded_parts.append(f"{count}{current_char}")
    else:
        encoded_parts.append(current_char)
        
    return "".join(encoded_parts)
            