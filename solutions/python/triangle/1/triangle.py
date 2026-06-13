def triangle(sides):
    #Appelé les côtés 
    a, b, c = sides    
    #Conditions que chaque côté est supérieur à 0 et que chaque somme de deux côtés d'un triangle est égale ou supérieur au troisième côté.
    return min(sides) > 0 and a + b >= c and b + c >= a and a + c >= b

def equilateral(sides):
    #Appelé les côtés
    a, b, c = sides
    # Chaque côté sont égaux
    return triangle(sides) and (a == b == c)


def isosceles(sides):
    a, b, c = sides 
    return triangle(sides) and ((a == b ) or ( b == c) or ( a == c ))


def scalene(sides):
    a, b, c = sides 
    return triangle(sides) and (a != b and a != c and b != c)
