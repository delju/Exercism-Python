
def is_armstrong_number(number):

    #Convertir le nombre en string
    number_str = str(number)
    #Calculer la longueur du nombre pour savoir la puissance à utiliser 
    number_len = len(number_str)
    
    # On initie la variable total qui est null au début
    total = 0

    #Boucle pour que chaque nombre soit multiplier la puissance et l'ajouter au reste
    for n in number_str: 
        result = int(n) ** number_len
        total = total + result 

    # Si le total est égal au nombre encodé alors le nombre est un nombre d'Amstrong
    if total == number: 
        return True
    else: 
        return False
