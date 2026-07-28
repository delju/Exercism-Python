"""
Exercice Python: House
"""

def recite(start_verse, end_verse):
    """
    Fonction qui va générer des couplets de la chanson en fonction de quel couplet demander.
    """

    song = [] 

    parts = [
        "the house that Jack built",
        "the malt that lay in", 
        "the rat that ate", 
        "the cat that killed", 
        "the dog that worried", 
        "the cow with the crumpled horn that tossed", 
        "the maiden all forlorn that milked", 
        "the man all tattered and torn that kissed", 
        "the priest all shaven and shorn that married", 
        "the rooster that crowed in the morn that woke", 
        "the farmer sowing his corn that kept", 
        "the horse and the hound and the horn that belonged to"
    ]

    #Boucle pour rechercher la partie correspondante
    for day in range(start_verse - 1, end_verse): 
        verse = f"This is "
        #Boucle pour ajouter le reste de la chanson en prenant les parties précédente
        for next_part in range(day, -1, -1): 
            verse += parts[next_part]
            if next_part > 0:
                verse += " "
        #Ajoute . à la fin.
        verse += "."
        song.append(verse)

    return song
        

