import operator

def convert(number):

    """ 
    Initié la variable qui donne le résultat 
    Si number divisible par 3 on ajoute Pling
    Si number divisible par 5 on ajoute Plang 
    Si number divisible par 7 on ajoute Plong 
    Si number n'est pas divisible par un de ces chiffres, on affiche le nombre en string
    """
    resultat = "" 
    
    if operator.mod(number, 3) == 0: 
        resultat += "Pling"
        
    if operator.mod(number, 5) == 0: 
        resultat += "Plang"
        
    if operator.mod(number, 7) == 0: 
        resultat += "Plong"
        
    if resultat == "": 
       return str(number)
    else: 
        return resultat

    
