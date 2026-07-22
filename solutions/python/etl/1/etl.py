"""
Exercice Python: ETL
"""

def transform(legacy_data):
    """
    Fonction qui va transformer la liste existante, en la triant par lettre et chaque lettre avec les points correspondant
    """
    new_data = {}
    #Boucle qui va parcourir les points et les lettres dans la liste existante
    for point, letters in legacy_data.items():
        #Pour chaque lettre récupérée 
        for just_letter in letters: 
            #On l'insert dans la nouvelle base de donnée, lettres en minuscule et les points qui lui correspondent
            new_data[just_letter.lower()] = point

    return new_data
        
