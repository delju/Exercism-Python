"""
Exercice Python: Saddle points
"""

def saddle_points(matrix):
    """
    Fonction qui permet de trouver un nombre dans une grille avec les conditions que ce soit le plus grand de la ligne et le plus petit de la colonne
    """
    #Si la grille est vide
    if not matrix: 
        return []
    #Si les lignes ou colonnes  ne sont pas de même longeur
    if any(len(line) != len(matrix[0]) for line in matrix):
        raise ValueError("irregular matrix")

    #Récupère les chiffres les plus grands des lignes et les plus petits des colonnes
    max_line = [max(line) for line in matrix]
    min_col = [min(col) for col in zip(*matrix)]

    point_found = [] 

    #Double boucle pour parcourir la grille et comparé les chiffres avec ceux récupérés 
    for index_line, value_line in enumerate(matrix): 
        for index_col, value_col in enumerate(value_line): 
            #Si ce sont les bons chiffres, on les ajoute au dict
            if value_col == max_line[index_line] and value_col == min_col[index_col]: 
                point_found.append({
                    "row": index_line + 1,
                    "column": index_col + 1
                })

    return point_found