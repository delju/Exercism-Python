"""
Exercice Python: Transpose
"""

from itertools import zip_longest

def transpose(text):
    """
    Fonction pour effectuer une transposition des lignes en colonnes
    """
    list_text = text.split("\n")

    result = []

    for column in zip_longest(*list_text, fillvalue="~"): 
        transposed_lines = "".join(column)
        transposed_lines = transposed_lines.rstrip("~").replace("~", " ")
        result.append(transposed_lines)

    return "\n".join(result)
