"""
Exercice python: Luhn
"""

class Luhn:
    """
    Classe pour la formule de Luhn
    """
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        """
        Fonction qui va valider si le code envoyé est valide selon la formule de luhn
        """
        #On nettoie le code en retirant les espaces
        clean_code = self.card_num.replace(" ", "")
        #Si le code est égale à 1 caractère ou moins, ou que ce n'est pas un chiffre, on retourne Faux
        if len(clean_code) <= 1 or not clean_code.isdigit(): 
            return False 

        total_sum = 0 
        #On inverse le code pour le lire de droite à gauche
        inverse_code = clean_code[::-1]
        #Boucle qui récupère l'index et le chiffre du code inversé
        for index, caracter in enumerate(inverse_code): 
            number = int(caracter)
            #Tout les deux chiffres, on double celui ci.
            if index % 2 == 1: 
                number = number * 2 
                #Si ce chiffre est plus grand que 9, on doit retirer 9 à la solution
                if number > 9: 
                    number = number - 9
            #On ajoute le chiffre à chaque tour au total
            total_sum += number
        #Si le total est un multiple de 10, on retourne vrai
        if total_sum % 10 == 0: 
            return True
        return False
        
                
    
