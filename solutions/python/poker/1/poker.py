"""
Exercice Python: Poker
"""

from collections import Counter

def best_hands(hands):
    """
    Déterminer quelles mains du jeu est la meilleure
    """
   
    def parser_main(hand_text):
        """Décode une main de poker"""
        # L'index de chaque caractère dans cette chaîne correspond pile à sa valeur mathématique !
        # Le 'X' sert juste à occuper l'index 10 pour le '10' de l'énoncé.
        order_cards = "..23456789XJQKA"
    
        # 1. On extrait et traduit les valeurs (on remplace le texte '10' par 'X' pour faire un seul caractère)
        values = sorted([order_cards.index(c[:-1].replace("10", "X")) for c in hand_text.split()], reverse=True)
    
        # 2. On extrait les couleurs
        colors = [card[-1] for card in hand_text.split()]
    
        # 3. L'astuce magique pour la quinte basse (A-2-3-4-5)
        if values == [14, 5, 4, 3, 2]:
            values = [5, 4, 3, 2, 1]
        
        return values, colors

    def mark_hand(hand_text): 
        """Attribue un tuple de notation (force, cartes) pour chaque main."""
        # 1. On récupère les éléments du parsing
        values, colors = parser_main(hand_text)
        # 2. Compte les fréquences et trie par importance (ex: la paire d'abord)
        value_counter = Counter(values)
        sorted_importance_values = [card for card, freq in value_counter.most_common()]
        sign_freq = [freq for card, freq in value_counter.most_common()]
        # 3. Détection des suites et des couleurs
        hand_color = len(set(colors)) == 1 
        hand_straight = len(set(values)) == 5 and (values[0] - values[4] == 4)
         # 4. On attribue la note de la combinaison (de 0 à 8)
        if hand_straight and hand_color:
            return (8, sorted_importance_values)  # Quinte Flush
        if sign_freq == [4, 1] :
            return (7, sorted_importance_values) #Carré
        if sign_freq == [3, 2] :
            return (6, sorted_importance_values) #Full 
        if hand_color:
            return (5, sorted_importance_values)  # Couleur
        if hand_straight:
            return (4, sorted_importance_values)  # Suite
        if sign_freq == [3, 1, 1] :
            return (3, sorted_importance_values) #Brelan
        if sign_freq == [2, 2, 1] :
            return (2, sorted_importance_values) # Double Paire
        if sign_freq == [2, 1, 1, 1] :
            return (1, sorted_importance_values) #Paire
    
        return (0, sorted_importance_values)
        
    # 1. On calcule la note maximale de toute la table
    max_note = max(mark_hand(main) for main in hands)
    
    # 2. On renvoie toutes les mains qui ont obtenu cette note maximale (gère les partages)
    return [main for main in hands if mark_hand(main) == max_note]