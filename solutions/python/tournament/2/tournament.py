"""
Exercice Python: Tournament 
"""

def tally(rows):
    """
    Fonction permettant de convertir les textes en un tableau lisible, triant les équipes par nombres de points et selon le nombre de match gagné. 
    """
    
    scores = {}

    #Boucle qui parcourt chaque ligne du texte
    for line in rows: 
        #On divise les éléments de la première ligne selon ; pour avoir l'équipe 1, l'équipe 2 et le résultat 
        team1, team2, result = line.split(";")
         #Si l'équipe 1 n'est pas dans le tableau, on l'insert avec les stats à 0
        if team1 not in scores: 
            scores[team1] = {"MP": 0, "W": 0, "D": 0, "L": 0, "P": 0}
        #Si l'équipe 2 n'est pas dans le tableau, on l'insert avec les stats à 0
        if team2 not in scores: 
            scores[team2] =  {"MP": 0, "W": 0, "D": 0, "L": 0, "P": 0}
        #Et on ajoute 1 au nombre de match joués
        scores[team1]["MP"] += 1
        scores[team2]["MP"] += 1
        #Si le résultat est win, on ajoute dans les colonnes correspondantes, la gagnant, le perdant et le nombre de point au gagnant
        if result == "win": 
            scores[team1]["W"] += 1
            scores[team2]["L"] += 1
            scores[team1]["P"] += 3
        #Si le résultat est loss, on ajoute dans les colonnes correspondantes, la gagnant, le perdant et le nombre de point au gagnant
        if result == "loss": 
            scores[team1]["L"] += 1
            scores[team2]["W"] += 1
            scores[team2]["P"] += 3
        #Si le résultat est draw, on ajoute dans les colonnes correspondantes aux équipes les matchs nulls et les points 
        if result == "draw":
            scores[team1]["D"] += 1
            scores[team2]["D"] += 1
            scores[team1]["P"] +=1
            scores[team2]["P"] += 1

    # On trie la liste des équipes (nom, stats)
    sorted_teams = sorted(scores.items(), key=lambda x: (-x[1]["P"], x[0]))

    #On initie le tableau d'affichage
    tableau = ["Team                           | MP |  W |  D |  L |  P"]
    #Pour chaque noms et stats du tableau triés
    for name, stats in sorted_teams:
        # On fabrique la ligne parfaitement alignée pour chaque équipe
        line = f"{name:<30} | {stats["MP"]:>2} | {stats["W"]:>2} | {stats["D"]:>2} | {stats["L"]:>2} | {stats["P"]:>2}"
        #On l'ajoute au tableau d'affichage
        tableau.append(line)
        
    return tableau
