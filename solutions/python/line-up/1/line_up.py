"""
Exercice Python: Line-up
"""

def line_up(name, number):
    """
    Fonction qui va créer une phrase selon le prénom et le numéro du client.
    """
    #Si les deux derniers chiffres sont coincés entre 11 et 13, on met th
    if 11 <= number % 100 <= 13: 
        suffix = "th"
    else: 
        #On me donne le dernier chiffre, on met th, sauf pour 1, 2 et 3
        last_number = number % 10
        suffix = "th"
        
        if last_number == 1: 
            suffix = "st"
        if last_number == 2: 
            suffix = "nd"
        if last_number == 3: 
            suffix = "rd"

    return f"{name}, you are the {number}{suffix} customer we serve today. Thank you!"
            
