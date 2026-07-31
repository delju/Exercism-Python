"""
Exercice Python: Phone Number
"""

class PhoneNumber:
    """
    Classe d'un numéro de téléphone
    """
    def __init__(self, number):
        #Boucle qui va permettre de parcourir chaque éléments du numéro de téléphone et envoyé un message d'erreur si on retrouve une lettre ou une ponctuation
        for char in number:
            if char.isalpha():
                raise ValueError("letters not permitted")
                
            if not char.isdigit() and char not in " +-.()":
                raise ValueError("punctuations not permitted")
        #On nettoie le numéro de téléphone     
        clean = "".join(char for char in number if char.isdigit())
        #Si il y a 11 chiffre, et que le premier nombre est 1, on découpe pour retirer le 1, si non on envoie un message d'erreur
        if len(clean ) == 11:
            if clean[0] == "1":
                clean = clean[1:] 
            else: 
                raise ValueError("11 digits must start with 1")
        #Si le numéro a moins de 10 ou plus de 11, on envoie un message d'erreur
        if len(clean) < 10:
            raise ValueError("must not be fewer than 10 digits")
        if len(clean) > 10: 
            raise ValueError("must not be greater than 11 digits")
            #Liste d'erreur si après avoir nettoyé, le premier ou le 4e chiffre sont 0 ou 1: 
            # 1. On définit nos règles : (Condition logique, Message d'erreur)
        validation_ruls = {
            clean[0] == "0": "area code cannot start with zero",
            clean[0] == "1": "area code cannot start with one",
            clean[3] == "0": "exchange code cannot start with zero",
            clean[3] == "1": "exchange code cannot start with one",
        }

        # 2. Une seule boucle vérifie tout d'un coup
        for error_condition, message in validation_ruls.items():
            if error_condition:
                raise ValueError(message)
                
        # 3. Si tout est valide, on enregistre
        self.number = clean
        self.area_code = clean[0:3]

    def pretty(self):
        """Renvoie le numéro mis en forme : (XXX)-XXX-XXXX."""
        # On découpe les trois morceaux du numéro de 10 chiffres
        prefixe = self.number[3:6]
        line = self.number[6:10]
        
        return f"({self.area_code})-{prefixe}-{line}"