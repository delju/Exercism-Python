def score(x, y):
    """
    Déterminer les points marqués lors d'un lancer dans une partie de fléchettes

    0 point : la fléche est hors zone 
    1 point: la fléche est dans un cercle d'un rayon compris entre 6 et 10
    5 point: la fléche est dans un cercle d'un rayon compris entre 1 et 5
    10 point: la fléche est dans un cercle d'un rayon de 0 (centre)
    
    """
    distance = (x**2 + y**2) ** 0.5

    if distance <= 1: 
        return 10  # On attrape tout ce qui est entre 0 et 1 (le 1 inclus !)
        
    if distance <= 5: 
        return 5   # On attrape tout le reste jusqu'à 5 (ex: 3.4 ou 5.0)
        
    if distance <= 10: 
        return 1   # On attrape tout le reste jusqu'à 10 (ex: 5.5 ou 9.9)
        
    return 0       # Tout ce qui est strictement plus grand que 10 prend 0 point
