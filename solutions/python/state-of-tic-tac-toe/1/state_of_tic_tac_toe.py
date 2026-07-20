"""
Exercice Python : state of tic-tac-toe
"""

def gamestate(board):
    """
    Fonction permettant de déterminer les états du jeu et de générer une erreur approprié si besoin
    """

    #On rassemble a liste en une chaine de caractère complete 
    flat_board = "".join(board)

    #On calcul le nombre de X et le nombre de O
    number_x = flat_board.count("X")
    number_O = flat_board.count("O")

    #Si Il y a plus de O que de X: O a joué en premier
    if number_O > number_x: 
        raise ValueError("Wrong turn order: O started")
    #Si il y a deux X ou plus que de O, X a jouer deux fois
    if number_x - number_O >= 2: 
        raise ValueError("Wrong turn order: X went twice")

    # 1. On sépare nos 3 lignes de texte pour y voir clair
    l1, l2, l3 = board[0], board[1], board[2]

    # 2. On fabrique les 8 chaînes de 3 caractères (lignes, colonnes, diagonales)
    combinaisons = [
        l1, l2, l3,                            # Horizontales
        l1[0] + l2[0] + l3[0],                 # Verticale 1
        l1[1] + l2[1] + l3[1],                 # Verticale 2
        l1[2] + l2[2] + l3[2],                 # Verticale 3
        l1[0] + l2[1] + l3[2],                 # Diagonale principale
        l1[2] + l2[1] + l3[0]                  # Diagonale secondaire
    ]

    # 3. On vérifie si un alignement complet existe
    x_win = "XXX" in combinaisons
    o_win = "OOO" in combinaisons

    #Les conditions: 1. Si X et O gagne, on renvoie une erreur
    if x_win and o_win: 
        raise ValueError("Impossible board: game should have ended after the game was won")
    #2. Renvoie Win si l'un ou l'autre gagne
    if x_win or o_win: 
        return "win"
    #Renvoie draw si il n'y a plus de blanc dans la grille et que personne ne gagne
    if not " " in flat_board: 
        return "draw"
    #Renvoie "ongoing" si le jeu est en cours  
    return "ongoing"


    
