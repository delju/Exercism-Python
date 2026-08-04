# Globals for the directions
# Change the values as you see fit
EAST = "EAST"
NORTH = "NORTH"
WEST = "WEST"
SOUTH = "SOUTH"

class Robot:
    """
    Classe pour un robot et son déplacement
    """
    directions = (NORTH, EAST, SOUTH, WEST)
    
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.coordinates = (x_pos, y_pos)


    def turn_right(self):
        """
        Fonction pour tourner de 90° à droite
        """
        # On l'utilise en l'appelant par le nom de la classe
        current_index = Robot.directions.index(self.direction)
        new_index = (current_index + 1) % 4
        self.direction = Robot.directions[new_index]

    def turn_left(self):
        """
        Fonction pour tourner de 90° à gauche
        """
        # Idem pour tourner à gauche
        current_index = Robot.directions.index(self.direction)
        # On soustrait 1 pour reculer dans le carrousel
        new_index = (current_index - 1) % 4
        self.direction = Robot.directions[new_index]

    def advance(self): 
        """
        Fonction pour avancer le robot d'une case dans sa direction actuel
        """
        x, y = self.coordinates

        movements = {
            NORTH: (0, 1),   # Le y augmente de 1
            SOUTH: (0, -1),  # Le y diminue de 1
            EAST: (1, 0),    # Le x augmente de 1
            WEST: (-1, 0)    # Le x diminue de 1
            }

        dx, dy = movements[self.direction]

        self.coordinates = (x + dx, y + dy)

    def move(self, orders): 
        """
        Fonction pour lire les instructions et déclencher les bonnes actions
        """

        for letter in orders: 
            if letter == "R": 
                self.turn_right()  
            elif letter == "L": 
                self.turn_left()
            elif letter == "A": 
                self.advance()

        
        
