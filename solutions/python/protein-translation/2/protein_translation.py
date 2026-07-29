"""
Exercice Python: Protein translation
"""

def proteins(strand):
    """
    Fonction qui permet de lire un codon et de la traduire en l'acide aminé qui lui correspond
    """
    codon_to_protein = {
    "AUG": "Methionine",
    "UUU": "Phenylalanine", "UUC": "Phenylalanine",
    "UUA": "Leucine", "UUG": "Leucine",
    "UCU": "Serine", "UCC": "Serine", "UCA": "Serine", "UCG": "Serine",
    "UAU": "Tyrosine", "UAC": "Tyrosine",
    "UGU": "Cysteine", "UGC": "Cysteine",
    "UGG": "Tryptophan",
    "UAA": "STOP", "UAG": "STOP", "UGA": "STOP"
    }

    result = []
    #Boucle for qui va parcourir les éléments 3 par 3, ajouter la réponse dans une liste et l'arrêter si un de ces éléments est un STOP
    for element in range(0, len(strand), 3):
        codon = strand[element:element+3]

        if codon_to_protein[codon] == "STOP": 
            break 

        result.append(codon_to_protein[codon])
    return result