"""
Exercice Python: food chain
"""

def recite(start_verse, end_verse):
    """
    Fonction qui va générer une chanson en fonction de la partie souhaitée. 
    """
    
    animals = ["fly", "spider", "bird", "cat", "dog", "goat", "cow", "horse"]
    specific_sentence = [
        "",  # Index 0 : La mouche
        "It wriggled and jiggled and tickled inside her.", # Index 1 : L'araignée
        "How absurd to swallow a bird!",                   # Index 2 : L'oiseau
        "Imagine that, to swallow a cat!",                 # Index 3 : Le chat
        "What a hog, to swallow a dog!",                   # Index 4 : Le chien
        "Just opened her throat and swallowed a goat!",    # Index 5 : La chèvre
        "I don't know how she swallowed a cow!",           # Index 6 : La vache
        "She's dead, of course!"                           # Index 7 : Le cheval
    ]
    song = []

    #Boucle qui va pour chaque jour demander 
    for day in range(start_verse - 1, end_verse): 
        verse = []
        #Ajouter la première phrase en fonction de l'animal
        verse.append(f"I know an old lady who swallowed a {animals[day]}.")
        #Si il y a une phrase spécifique à l'animal on l'ajoute
        if specific_sentence[day]: 
            verse.append(specific_sentence[day])

        # Si c'est le cheval, on gère sa fin et on passe directement au couplet suivant
        if day == 7: 
            song.extend(verse)
            if day < (end_verse - 1):
                song.append("")
            continue 

        # Pour tous les autres animaux, on fait la cascade
        for each in range(day, 0, -1):
            #Si c'est l'araignée, il y a une phrase en plus.
            if animals[each - 1] == "spider": 
                #On met bien la phrase entière avec "She swallowed the bird..."
                verse.append("She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.")
            #Si non, on mets la phrase de base.
            else: 
                verse.append(f"She swallowed the {animals[each]} to catch the {animals[each - 1]}.")

        # La phrase de conclusion de la mouche
        verse.append("I don't know why she swallowed the fly. Perhaps she'll die.")
        
        # On ajoute le couplet à la chanson
        song.extend(verse)
    
        # Ajout de la ligne vide entre les couplets
        if day < (end_verse - 1):
            song.append("")

    
    return song