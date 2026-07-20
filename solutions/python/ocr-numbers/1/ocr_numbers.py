"""
Exercice Python: OCR numbers. 
"""

def convert(input_grid):
    """Convertir les chiffres dessiner à l'aide de "|", "_" et de " " en chiffre numérique"""

    #Si la grille est vide
    if not input_grid: 
        raise ValueError("Number of input lines is not a multiple of four.")

    #On récupére le nombre de lignes et le nombre de colonnes
    row = len(input_grid)
    column = len(input_grid[0])

    # Si le nombre de ligne n'est pas un mutliple de 4, message d'erreur
    if row % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")

    if column % 3 != 0:
        raise ValueError("Number of input columns is not a multiple of three")

    #Dictionnaire des différents chiffres
    digits = {
        (" _ ", 
         "| |", 
         "|_|", 
         "   "): "0",
     
        ("   ", 
         "  |", 
         "  |", 
         "   "): "1",
     
        (" _ ", 
         " _|", 
         "|_ ", 
         "   "): "2",
     
        (" _ ", 
         " _|", 
         " _|", 
         "   "): "3",
     
        ("   ", 
         "|_|", 
         "  |", 
         "   "): "4",
     
        (" _ ", 
         "|_ ", 
         " _|", 
         "   "): "5",
     
        (" _ ", 
         "|_ ", 
         "|_|", 
         "   "): "6",
     
        (" _ ", 
         "  |", 
         "  |", 
         "   "): "7",
     
        (" _ ", 
         "|_|", 
         "|_|", 
         "   "): "8",
     
        (" _ ", 
         "|_|", 
         " _|", 
         "   "): "9"
    }

    tot_line_number = []
    #Boucle, On récupère les 4 premières lignes 
    for line in range(0, row, 4): 
        lines_block = input_grid[line:line+4]

        line_number = ""
        #Boucle pour parcourir les colonnes de 3 en 3
        for col in range(0, column, 3): 
            #On extrait la grille de 3x4 caractère
            line_1 = lines_block[0][col:col+3]
            line_2 = lines_block[1][col:col+3]
            line_3 = lines_block[2][col:col+3]
            line_4 = lines_block[3][col:col+3]

            #On rassemble ces 4 lignes
            number_key = (line_1, line_2, line_3, line_4)

            #Si le nombre est dans la liste, on l'ajoute dans la séquence si non, on ajoute ?
            if number_key in digits: 
                line_number += digits[number_key]
            else:
                line_number += "?"
        #On ajoute le block dans la liste totat
        tot_line_number.append(line_number)
    #On retourne les chiffres avec une virgule qui sépare chaque blocks 
    return ",".join(tot_line_number)
        