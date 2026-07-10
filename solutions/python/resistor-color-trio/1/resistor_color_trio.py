""" Exercice Python Trio de couleurs de résistance 
color = liste de 10 couleurs, l'index correspondant au code de la couleur
"""
color = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

def label(colors):
    
    color_one = color.index(colors[0])
    color_two = color.index(colors[1])
    color_three = color.index(colors[2])

    value = (color_one * 10 + color_two) * (10 ** color_three)

    if value >= 1_000_000_000:
        return f"{value // 1_000_000_000} gigaohms"
    elif value >= 1_000_000: 
        return f"{value // 1_000_000} megaohms"
    elif value >= 1_000: 
        return f"{value // 1_000} kiloohms" 
    else: 
        return f"{value} ohms"
