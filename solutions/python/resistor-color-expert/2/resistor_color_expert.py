""" Exercice Python Expert en couleurs de résistance 
color = liste de 10 couleurs, l'index correspondant au code de la couleur
tolerance = list des couleurs avec leur taux de tolérence 
"""
color = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
tolerance = {
    "grey":"±0.05%", 
    "violet":"±0.1%", 
    "blue":"±0.25%", 
    "green":"±0.5%",
    "brown":"±1%",
    "red":"±2%", 
    "gold":"±5%", 
    "silver":"±10%" 
}


def calcul_brut_value(number_band, mutliplicator_band):
    """ Fonction qui permet de calculer la valeur de base """
    number = [color.index(c) for c in number_band]
    multiplicator = color.index(mutliplicator_band)

    base_value = 0
    for c in number:
        base_value = base_value * 10 + c

    return base_value * (10 ** multiplicator)
        
def resistor_label(colors):
    """
    Fonction traduisant les couleurs en une étiquette ohms + tolérance
    """
    if len(colors) == 1:  
        return f"{color.index(colors[0])} ohms"
        
    tolerance_number = tolerance[colors[-1]]

    if len(colors) == 4:
        value = calcul_brut_value(colors[0:2], colors[2])

    if len(colors) == 5: 
        value = calcul_brut_value(colors[0:3], colors[3])
        
        
    if value >= 1_000_000_000:
        return f"{(value / 1_000_000_000):g} gigaohms {tolerance_number}"
    if value >= 1_000_000: 
        return f"{(value / 1_000_000):g} megaohms {tolerance_number}"
    if value >= 1_000: 
        return f"{(value / 1_000):g} kiloohms {tolerance_number}" 
    return f"{value:g} ohms {tolerance_number}"
