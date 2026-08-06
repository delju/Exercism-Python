"""
Exercice Python: KinderGarten Garden
"""

class Garden:
    """
    Classe d'un jardin dans une classe d'enfant
    """
    def __init__(self, diagram, students = None):
        self.rows = diagram.split("\n") 

        if students is None: 
            self.students = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]

        else: 
            self.students = sorted(students)
    
    def plants(self, student): 
        """
        Fonction qui va permettre de retrouver les plantes de chaque enfants donnés 
        """
        
        plants_dict = {"V": "Violets", "R": "Radishes", "C": "Clover", "G": "Grass"}
        list_plant = []
        index_child = self.students.index(student) 
        
        return [plants_dict[letter] for line in self.rows for letter in line[2 * index_child : 2 * index_child + 2]]
                
                
            
        
