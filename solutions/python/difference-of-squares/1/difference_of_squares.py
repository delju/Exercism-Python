"""
Exercice Python: Difference of squares
"""

def square_of_sum(number):
    """
    Fonction qui permet de calculer le carré de la somme des nombres naturels
    """
    return sum(range(1, number + 1)) ** 2 


def sum_of_squares(number):
    """
    Fonction qui permet de caculuer la somme des carrés des nombres naturels
    """
    return sum(each**2 for each in range(1, number+1))


def difference_of_squares(number):
    """
    Fonction qui calcule la différences entre square of sum et sum of square
    """
    return square_of_sum(number) - sum_of_squares(number)
