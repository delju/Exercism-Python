"""
Exercice Python; Space Age
"""

class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds

    def on_earth(self):
        return round(self.seconds / 31557600, 2 )

    def on_mercury(self): 
        # On prend l'âge terrestre brut (sans arrondi) et on le divise par le ratio
        age_brut = (self.seconds / 31557600) / 0.2408467
        return round(age_brut, 2)

    def on_venus(self): 
        age_brut = (self.seconds / 31557600) / 0.61519726
        return round(age_brut, 2)

    def on_mars(self): 
        age_brut = (self.seconds / 31557600) / 1.8808158
        return round(age_brut, 2)

    def on_jupiter(self): 
        age_brut = (self.seconds / 31557600) / 11.862615
        return round(age_brut, 2)

    def on_saturn(self): 
        age_brut = (self.seconds / 31557600) / 29.447498
        return round(age_brut, 2)

    def on_uranus(self): 
        age_brut = (self.seconds / 31557600) / 84.016846
        return round(age_brut, 2)

    def on_neptune(self): 
        age_brut = (self.seconds / 31557600) / 164.79132
        return round(age_brut, 2)