"""
Exercice python secret handshake 
En fonction du code binaire donné, une action est déterminée pour chaque emplacement où il y a marqué 1. 
"""

def commands(binary_str):

    #On inverse le code donnée pour avoir plus facile.
    binary = binary_str[::-1]

    #On ajoute une liste vide pour ajouter les actions correspondant au code.
    actions = []
    
    if binary[0] == "1": 
        actions.append("wink")
    if binary[1] == "1": 
        actions.append("double blink")
    if binary[2] == "1": 
        actions.append("close your eyes")
    if binary[3] == "1": 
        actions.append("jump")
    if binary[4] == "1": 
        actions.reverse() 
        
    return actions 
