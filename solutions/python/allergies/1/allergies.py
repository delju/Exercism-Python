"""
Exercice Python: Allergies
"""

class Allergies:
    """
    Classe pour les allergies selon un score
    """

    def __init__(self, score):
        self.score = score

    allergens = ["eggs", "peanuts", "shellfish", "strawberries", "tomatoes", "chocolate", "pollen", "cats"]

    def allergic_to(self, item):
        """
        Fonction pour déterminer la personne est allergique à un aliment selon le score
        """
        index = Allergies.allergens.index(item)
        allergen_value = 1 << index
        return (self.score & allergen_value) > 0

    @property
    def lst(self):
        """
        Fonction qui permet de retourner une liste de tout les allergènes selon le score
        """
        return [all for all in Allergies.allergens if self.allergic_to(all)]
