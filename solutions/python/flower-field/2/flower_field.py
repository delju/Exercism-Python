"""
Exercice Python Flower Field: Principe du jeu Démineur. 
"""

def annotate(garden):
     
    """ 
    Fonction permettant de parcourir chaque élément afin de déterminer le nombres de fleurs autour de la clase à la vertical, à l'horizontal et à la diagonal 
    Variable pour avoir une liste des coordonnées des voisins
    """
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1), 
        (1, -1),  (1, 0),  (1,1)
    ]
    
    #Vérification que l'entrée n'est pas vide, que toutes les lignes sont de la même longueur et que chaque ligne ne contient que des espaces ou des fleurs "*" 
    if not garden:
        return [] 

    len_garden = len(garden[0]) 

    for line_garden in garden: 
        if len(line_garden) != len_garden: 
            raise ValueError("The board is invalid with current input.")

        for caractere in line_garden: 
            if caractere not in (" ", "*"): 
                raise ValueError("The board is invalid with current input.")

    #Variable pour créer une liste ne contenant que des caractères
    grid = [list(line_garden) for line_garden in garden]
    #Variable qui calcul la hauteur de la grille
    garden_height = len(grid) 
    #Variable qui calcul la longueur de la grille
    garden_larger = len(grid[0]) 

    """Double boucle qui va parcourir chaque élément de la grille, les lignes (row) et les colonnes (column) """

    for row in range(garden_height):
        for column in range(garden_larger):

            #Si c'est une fleur, on continue
            if grid[row][column] == "*": 
                continue 
            #Initie le compteur du nombre de fleur
            total_flower = 0
            #Pour chaque coordonnées de direction, on détermine les voisins
            for direction_r, direction_c in directions: 
                neighbor_r = row + direction_r 
                neighbor_c = column + direction_c 

                #Si cela reste dans les limites de la grilles
                if 0 <= neighbor_r < garden_height and 0 <= neighbor_c < garden_larger:
                    #Si c'est une fleur on augmente de 1 le compteur
                    if grid[neighbor_r][neighbor_c] == "*":
                        total_flower += 1
            #Si le nombre est plus grand que 0, alors on encode le chiffre à l'emplacement 
            if total_flower > 0:
                grid[row][column] = str(total_flower)
    #Enfin, on transforme la liste de la liste en une liste de chaine de caractère 
    return ["".join(line) for line in grid]


                
    
