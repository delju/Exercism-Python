"""
Exercice Python: Pythagorean triplet
"""

def triplets_with_sum(number):
    """Trouve les triplets éligibles au théorème de Pythagore pour une somme donnée."""
    triplets = []

    # UNE SEULE BOUCLE : On fait juste varier 'a'
    for num_a in range(1, (number // 3) + 1):
        numerateur = number**2 - 2 * number * num_a
        denominateur = 2 * (number - num_a)

        # Si b est un entier parfait
        if numerateur % denominateur == 0:
            num_b = numerateur // denominateur
            num_c = number - num_a - num_b

            # On vérifie que les nombres sont bien dans le bon ordre croissant
            if num_a < num_b < num_c:
                triplets.append([num_a, num_b, num_c])

    return triplets