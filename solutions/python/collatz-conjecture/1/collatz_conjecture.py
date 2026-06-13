def steps(number):

    #Confirmer que le nombre est entier et non null 
    if number <= 0: 
        raise ValueError("Only positive integers are allowed")

    #Initier la variable du compteur à 0 
    number_step = 0

    #Tant que le nombre est différent de 1 la boucle continue
    while number != 1:

        #Si le nombre est pair, on divise pas 2
        if number % 2 == 0: 
            number = number // 2 
        #Si le nombre est impair on multiplie par 3 et on ajoute 1
        else: 
           number = number * 3 + 1
        #Et on ajoute +1 aux nombres d'étapes
        number_step = number_step + 1 

    return number_step
        
        
