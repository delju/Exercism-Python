"""
Convertion des différents chiffres en base d'entrée et base de sortie
"""

def rebase(input_base, digits, output_base):

    #Vérification que chaque élément rentré rentre dans les conditions

    if input_base < 2: 
        raise ValueError("input base must be >= 2")
        
    if output_base < 2: 
        raise ValueError("output base must be >= 2")
    
    for number in digits:
        if number < 0 or number >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")

    #Convertion en base 10, la valeur brute

    brut_value = 0 

    for number in digits: 
        brut_value = (brut_value * input_base) + number 

    #convertion en base de sortie
    result = []
    while brut_value > 0: 
        rest = brut_value % output_base     
        result.insert(0, rest)
        brut_value = brut_value // output_base  

    if not result:
        return [0]

    return result
        
        
    

    
