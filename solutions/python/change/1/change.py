"""
Exercice Python: Change. 
"""

def find_fewest_coins(coins, target):
    """
    Retourne le nombre minimum de pièces pour atteindre la valeur demandée. 
    """
    # Si le target est inférieur, on renvoie une erreur
    if target < 0: 
        raise ValueError("target can't be negative")
        
    # Si la target est plus grand que 0, mais plus petit que la pièce la plus petite
    if 0 < target < coins[0]: 
        raise ValueError("can't make target with given coins")

    # Si le montant demandé est 0, on renvoie une liste vide.
    if target == 0: 
        return []

    optimal_combinations = [None] * (target + 1)
    optimal_combinations[0] = []

    # Boucle pour parcourir tous les montants jusqu'à la valeur de target
    for current_sum in range(1, target + 1):
        # Boucle pour chaque piece disponible 
        for piece in coins: 
            # Si la pièce est plus grande que le montant, on ne peut pas l'utiliser. 
            if piece > current_sum: 
                continue 

            rest = current_sum - piece 

            # La combinaison pour le reste doit exister
            if optimal_combinations[rest] is not None: 
                new_combination = optimal_combinations[rest] + [piece]    
                
                # Si la case est vide, ou que la nouvelle combinaison est plus courte 
                if optimal_combinations[current_sum] is None or len(new_combination) < len(optimal_combinations[current_sum]):
                    optimal_combinations[current_sum] = new_combination
    
    # Le test est sorti des boucles et vérifie si la case est restée à None
    if optimal_combinations[target] is None: 
        raise ValueError("can't make target with given coins")

    #On trie la liste du plus grand au plus petit 
    optimal_combinations[target].sort()

    #On retourne la liste 
    return optimal_combinations[target]
