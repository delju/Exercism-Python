"""
Exercice Python: Gigasecond
"""
from datetime import timedelta 

def add(moment):
    """
    Fonction qui va calculer deux dates avec un écart d'une gigaseconde
    """
    return moment + timedelta(seconds = 10**9)
