def square(number):
    """Calcule le nombre de grains sur une case spécifique (de 1 à 64)."""
    # Validation logique de la saisie
    if not 1 <= number <= 64:
        raise ValueError("square must be between 1 and 64")
        
    # Mathématiquement : la case 1 est 2^0, la case 2 est 2^1, etc.
    return 2 ** (number - 1)


def total():
    """Calcule le nombre total de grains sur l'intégralité de l'échiquier (64 cases)."""
    # Formule mathématique rapide : la somme de 2^0 + 2^1 + ... + 2^63 est égale à (2^64) - 1
    return (2 ** 64) - 1
