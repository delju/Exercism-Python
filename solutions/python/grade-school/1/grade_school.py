"""
Exercice Python: Grade School
"""
from collections import defaultdict

class School:
    """
    Classe pour gérer une liste d'élèves
    """
    
    def __init__(self):
        self.grades = defaultdict(list)
        self.students_registry = set()
        self.add_log = []

    def add_student(self, name, grade):
        """
        Fonction pour ajouter un étudiant et son grade si il n'est pas encore dans la liste
        """
        if name in self.students_registry:
            self.add_log.append(False)
            return "Student is already in the school."
        self.grades[grade].append(name)
        self.students_registry.add(name)
        self.add_log.append(True)
        return f"Added {name} to grade {grade}."

    def roster(self):
        """
        Fonction qui renvoie une liste de tout les élèves par grade et par ordre alphabétique
        """
        all_school = []
        for level in sorted(self.grades.keys()): 
            all_school.extend(self.grade(level))
        return all_school

    def grade(self, grade_number):
        """
        Fonction qui renvoie une liste des élèves selon leurs grades
        """
        return sorted(self.grades[grade_number])

    def added(self):
        """
        Renvoie une liste d'historique de réussite des tentatives d'ajouts
        """
        return self.add_log