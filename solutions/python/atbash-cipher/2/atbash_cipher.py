"""
Exercice python chiffre d'Atbash 

Fonction pour chiffré le text, inversion des lettres + découper en bloc de 5 lettres
"""

def encode(plain_text):
    letters = [caractere for caractere in plain_text.lower() if caractere.isalnum()]

    clean_letters = "".join(letters)
    translated = str.maketrans("abcdefghijklmnopqrstuvwxyz", "zyxwvutsrqponmlkjihgfedcba")

    text_translate = clean_letters.translate(translated)

    result = []
    for i in range(0, len(text_translate), 5): 
        result.append(text_translate[i:i+5])
    return " ".join(result)

    
"""
Fonction permettant de décoder les éléments inversés mais sans espace...
"""
def decode(ciphered_text):

    letters = [caractere for caractere in ciphered_text if caractere.isalnum()]
    clean_letters = "".join(letters) 

    translated = str.maketrans("zyxwvutsrqponmlkjihgfedcba", "abcdefghijklmnopqrstuvwxyz")

    return clean_letters.translate(translated)
    
    
