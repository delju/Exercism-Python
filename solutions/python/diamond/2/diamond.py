"""
Exercice Python Diamant: Créer un losange à partir de la place de la lettre encodée. Ce losange doit commencer par A et terminer par A.
"""

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def rows(letter):

    #Trouver l'index max de la lettre encodée
    index_max = alphabet.index(letter)

    lines = []
    # Jusqu'à cette lettre, on regarde chaque lettre et on calcul les espaces intérieurs et extérieurs
    for index, lettre in enumerate(alphabet[:index_max + 1]): 

        if index == 0: 
            out_space = " " * index_max 
            line = out_space + "A" + out_space

        else: 
            out_space = " " * (index_max - index) 
            inner_space = " " * (2 * index - 1)

            line = out_space + lettre + inner_space + lettre + out_space

        #Chaque ligne est encodée dans la liste 
        lines.append(line)

    #On retourne la liste, ainsi que la liste inversée sans le dernier élément qui ne doit être présenté qu'une fois
    return lines + lines[:-1][::-1]

    