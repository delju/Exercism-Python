"""
Exercice Python: High Scores
"""

class HighScores:
    """
    Classe sur les scores du jeu Frogger
    """
    def __init__(self, scores):
        self.scores = scores 

    def latest(self): 
        """
        Fonction qui renvoie le dernier score enregistré
        """
        return self.scores[-1] 

    def personal_best(self): 
        """
        Fonction qui renvoie le meilleur score de la liste
        """
        return max(self.scores)

    def personal_top_three(self): 
        """
        Fonction qui renvoie les trois meilleurs scores de la liste
        """
        tried_scores = sorted(self.scores, reverse = True)
        return tried_scores[:3]
    
