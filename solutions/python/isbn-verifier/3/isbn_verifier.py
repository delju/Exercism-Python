def is_valid(isbn):

    """
    Vérifier que l'isbn soit valide: 
    Récupérer chaque chiffre et le mutliplier par la valeur de l'indexe inversé
    attention le dernier chiffre est un caractère de contrôle qui est un chiffre ou un X qui vaut 10
    L'isbn doit comprendre 10 caractères, les 9 premiers des chiffres et le dernier un chiffre ou un X
    """
    # 1. Le nettoyage
    isbn_clean = isbn.replace("-", "")

    # 2. Les filtres de sécurité (On élimine les faux)
    if len(isbn_clean) != 10:
        return False
        
    if not isbn_clean[:9].isdigit():
        return False
        
    if not (isbn_clean[9].isdigit() or isbn_clean[9] == "X"):
        return False

    # 3. Le calcul 
    poids = range(10, 0, -1)
    total_sum = 0
    for caractere, multiplicator in zip(isbn_clean, poids):
        valeur = 10 if caractere == "X" else int(caractere)
        etape = valeur * multiplicator
        total_sum += etape

    return total_sum % 11 == 0
