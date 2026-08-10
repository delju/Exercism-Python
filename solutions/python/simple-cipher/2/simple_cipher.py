"""
Exercice Python: Simple cipher
"""
import random
import string

class Cipher:
    """
    Classe pour chiffrer et déchiffrer selon le chiffrement de Vigenère
    """
    def __init__(self, key=None):
        if key is None: 
            self.key = "".join(random.choice(string.ascii_lowercase) for _ in range(100))
        else: 
            self.key = key
            

    def encode(self, text):
        """Encode le texte en utilisant la clé du chiffrement."""
        result= []
        
        for index, letter in enumerate(text): 
            #On trouve la clé selon l'index
            letter_key = self.key[index % len(self.key)]
            #L'écart entre la lettre et le a
            gap = ord(letter_key) - ord("a")
            #On calcul pour avoir la nouvelle lettre avec un modulo 26 pour revenir à a après z
            new_code = (ord(letter) - ord("a") + gap) % 26 + ord("a")
            result.append(chr(new_code))
            
        return "".join(result)
            
    def decode(self, text):
        """Décode le texte en utilisant la clé du chiffrement."""
        result= []
        
        for index, letter in enumerate(text): 
            letter_key = self.key[index % len(self.key)]
            gap = ord(letter_key) - ord("a")
            new_code = (ord(letter) - ord("a") - gap) % 26 + ord("a")
            result.append(chr(new_code))
            
        return "".join(result)
