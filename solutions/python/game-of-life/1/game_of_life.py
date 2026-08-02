"""
Exercice Python: Game of life 
"""

def tick(matrix):
    """
    Fonction qui génère la génération suivante du jeu La vie de Conway
    """
    if not matrix or not matrix[0]:
        return []

    #On calcul les longueurs des lignes et des colonnes 
    line = len(matrix)
    column = len(matrix) if line > 0 else 0 

    #On crée une copie de la grille
    next_gen = [[0] * column for index_line in range(line)]

    for row in range(line):
        for col in range(column): 
            #Compteur des cellules vivantes
            live_cell = 0 
            #Sécurité des bordures de la grilles
            start_line = max(0, row - 1)
            end_line = min(line - 1, row + 1)
            start_column = max(0, col - 1)
            end_column = min(column - 1, col + 1)

            #On parcourt la mini grille des voisins
            
            for neight_line in range(start_line, end_line + 1): 
                for neight_col in range(start_column, end_column + 1): 
                    #On ne doit pas se compter soi-même
                    if neight_line == row and neight_col == col:
                        continue 

                    #Si la case voisine est vivante 
                    if matrix[neight_line][neight_col] == 1: 
                        live_cell += 1
                        
            #Si la cellule est vivante et qu'elle a 2 ou 3 voisines vivantes
            if matrix[row][col] == 1 and live_cell in (2, 3):
                next_gen[row][col] = 1
                
            # Règle de naissance : si elle est morte ET a exactement 3 voisins
            elif matrix[row][col] == 0 and live_cell == 3:
                next_gen[row][col] = 1

    return next_gen
        

    
