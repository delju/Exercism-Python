"""
Exercice Python: twelve days
"""

def recite(start_verse, end_verse):
    """ 
    Fonction permettant de générer la chanson au jour choisi 
    """

    ordinal = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth" ]

    gifts = [
        "a Partridge in a Pear Tree.", 
        "two Turtle Doves, ", 
        "three French Hens, ",
        "four Calling Birds, ", 
        "five Gold Rings, ", 
        "six Geese-a-Laying, ", 
        "seven Swans-a-Swimming, ", 
        "eight Maids-a-Milking, ", 
        "nine Ladies Dancing, ", 
        "ten Lords-a-Leaping, ", 
        "eleven Pipers Piping, ", 
        "twelve Drummers Drumming, "
    ]
    #Initie la liste des résultats
    result = []

    #Boucle qui va démarré à partir du premier jour, jusqu'au dernier jour
    for day in range(start_verse - 1, end_verse):
        #On initie le verse avec le nombre ordinal du jour demandé
        verse = f"On the {ordinal[day]} day of Christmas my true love gave to me: "
        #Boucle qui va ajouter les cadeaux dans l'odre inversé pour commencer par le cadeau le plus loin, et finir par le premier cadeau.
        for gift_day in range(day, -1, -1):
            #Si c'est le premier jour, on ajoute le premier cadeau, sans and
            if day == 0: 
                verse += gifts[gift_day]
            #Si on est au dernier jour et qu'il y en a d'autre, il faut l'ajouter avec un and
            elif gift_day == 0:
                verse += "and " + gifts[gift_day]
            #Les cadeaux intermédiaire 
            else: 
                verse += gifts[gift_day]
        #On ajoute le verse dans la liste des résultats
        result.append(verse) 
    #On retourne cette liste
    return result
        
            