"""
Exercice Python: bottle song 
"""

def recite(start, take=1):
    """
    Fonction permettant de générer un texte, selon où tu veux démarrer dans la chanson et de combien de couplet tu veux afficher 
    """

    NUMBERS = ["no", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]

    song = []

    #Boucle qui va parcourir chaque élément, à l'envers, en commençant selon la demande
    for current_bottles in range(start, start - take, -1):

             # 1. Pour le présent (Lignes 1, 2 et 3 du couplet)
        if current_bottles == 1:
            word_now = "bottle"
        else:
            word_now = "bottles"

        # 2. Pour le futur / le reste (Ligne 4 du couplet)
        remaining = current_bottles - 1
        if remaining == 1:
            word_next = "bottle"
        else:
            word_next = "bottles"

         # On récupère le mot du nombre et on lui met une majuscule
        capitelize_numbers = NUMBERS[current_bottles].capitalize()
        
        # On ajoute la ligne 1, puis la ligne 2
        song.append(f"{capitelize_numbers} green {word_now} hanging on the wall,")
        song.append(f"{capitelize_numbers} green {word_now} hanging on the wall,")

        #On ajoute la ligne 3
        song.append(f"And if one green bottle should accidentally fall,")

        #On ajoute la ligne 4
        song.append(f"There'll be {NUMBERS[remaining]} green {word_next} hanging on the wall.")

        # Si le numéro actuel est plus grand que le point d'arrivée final,
        # cela signifie qu'il y a encore un autre couplet après celui-ci et on ajoute un espace
        if current_bottles > (start - take + 1):
            song.append("")

    return song