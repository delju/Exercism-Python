"""
Exercice Python: Yacht
"""

from collections import Counter

# Score categories.
# Change the values as you see fit.
YACHT = "yacht"
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = "full_house"
FOUR_OF_A_KIND = "four_of_a_kind"
LITTLE_STRAIGHT = "little_straight"
BIG_STRAIGHT = "big_straight"
CHOICE = "choice"

def score(dice, category):
    """
    Fonction qui calcule les points selon la catégorie du jeu et les dès donnés
    """
    #Si la catégorie fait partie de ceux ci, on multiplie le nombre de dé lié à la catégorie * ce nombre
    if category in (ONES, TWOS, THREES, FOURS, FIVES, SIXES): 
        return category * dice.count(category)
    

    #Si catégorie est Choice, on fait simplement une somme de tout les dés
    if category == CHOICE:
        return sum(dice)

    #Si c'est la petite suite, c'est 30 points
    if category == LITTLE_STRAIGHT: 
        return 30 * (sorted(dice) == list(range(1, 6)))

    #Pareil pour la grande suite
    if category == BIG_STRAIGHT: 
        return 30 * (sorted(dice) == list(range(2,7)))

    #Si c'est un full, on fait la somme des dés
    if category == FULL_HOUSE:
        counts = Counter(dice)
        # Si on a bien un groupe de 2 et un groupe de 3 dés identiques
        if sorted(counts.values()) == [2, 3]:
            return sum(dice)
        return 0
    #Si c'est un carré, c'est 4 fois le dés
    if category == FOUR_OF_A_KIND:
        counts = Counter(dice)
        # On récupère le dé le plus fréquent et son nombre d'apparitions
        most_frequency, number_occurence = counts.most_common(1)[0]
        
        # S'il apparaît 4 fois ou 5 fois (un Yacht compte aussi comme un carré !)
        if number_occurence >= 4:
            return most_frequency * 4
        return 0
    #Le yacht, c'est 50 points
    if category == YACHT:
        # Si l'ensemble n'a qu'un seul élément, c'est que tous les dés sont pareils !
        if len(set(dice)) == 1:
            return 50
        return 0