def is_valid(isbn):
    """ 1. Le nettoyage"""
    isbn_clean = isbn.replace("-", "")

    """ 2. Les filtres de sécurité (On élimine les faux)"""
    if len(isbn_clean) != 10:
        return False
        
    if not isbn_clean[:9].isdigit():
        return False
        
    if not (isbn_clean[9].isdigit() or isbn_clean[9] == "X"):
        return False

    """ 3. Le calcul """
    poids = range(10, 0, -1)
    total_sum = 0
    for caractere, multiplicator in zip(isbn_clean, poids):
        valeur = 10 if caractere == "X" else int(caractere)
        etape = valeur * multiplicator
        total_sum += etape

    return total_sum % 11 == 0
