"""
Exercice Python: Roman numerals
"""

def roman(number):
    """
    Fonction permettant de convertir un chiffre décimal en chiffre Romain
    """
    correspondence = {
        1000: "M", 900: "CM", 500: "D", 400: "CD",
        100: "C", 90: "XC", 50: "L", 40: "XL",
        10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"
    }

    #On initie la variable qui va garder le résultat
    result = ""

    #Pour chaque valeur est symbole du dictionnaire correspondence
    for value, symbol in correspondence.items():
        #tant que le nombre est plus grand ou égale à un nombre du dictionnaire, on ajoute le symbole au résultat et on retire, ensuite, la valeur au nombre
        while number >= value: 
            result += symbol 
            number -= value

    return result