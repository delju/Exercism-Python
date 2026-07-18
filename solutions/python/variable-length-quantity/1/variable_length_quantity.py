"""
Exercice python : Variable lenght quantity
"""

def encode(numbers):
    """
    Convertir le nombre en VLQ 
    """
    total_byte = []

    #Isoler le dernier nombre 
    for num in numbers: 
        num_byte = []

        #Extraction des 7 premiers bites 
        last_piece = num & 0x7F

        #Insertion du morceau dans la liste 
        num_byte.insert(0, last_piece)

        #Décalage du nombre de 7 bites
        num >>=7

        # Tant que c'est supérieur à 0, on s'occupe des morceaux suivants
        while num > 0: 
            #Extraction des 7 prochains bites 
            piece = num & 0x7F

            #Ajout de l'interrupteur (+0X80)
            piece_switch = piece + 0x80 

            #Insertion de ce morceau dans la liste
            num_byte.insert(0, piece_switch)

            #Décalage du nombre de 7 bites
            num >>=7 

        #Une fois la boucle while terminer on ajoute le tout à la fin de la liste 
        total_byte.extend(num_byte)

    return total_byte
        

def decode(bytes_):
    """Décoder les éléments pour le transformer en un nombre """

    #Message d'erreur si le dernier n'est pas fermé 
    if bytes_[-1] >= 0x80: 
        raise ValueError("incomplete sequence")

    decode_num = []

    current_number = 0 

    for num_octet in bytes_: 
        # 1. On décale notre total actuel vers la gauche pour libérer 7 places
        current_number <<= 7
    
        # 2. On nettoie l'octet reçu et on l'ajoute directement au total
        current_number += (num_octet & 0x7F)

        #3. Une fois que le nombre est terminer, on l'ajoute au numéro et on réinitialise le current_number pour le suivant 
        if num_octet < 0x80: 
            decode_num.append(current_number)
            current_number = 0 

    return decode_num
        
        

