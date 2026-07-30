"""
Exercice Python: Say
"""

def say(number):
    """
    Fonction pour convertir des nombres entier en lettre anglaise
    """
    num_ones = {0: "zero", 
            1: "one", 
            2: "two", 
            3: "three", 
            4: "four", 
            5: "five", 
            6: "six", 
            7: "seven", 
            8: "eight", 
            9: "nine"}
    num_teens = {10: "ten", 
             11: "eleven", 
             12: "twelve", 
             13: "thirteen", 
             14: "fourteen", 
             15: "fifteen", 
             16: "sixteen", 
             17: "seventeen", 
             18: "eighteen", 
             19: "nineteen"}
    num_tens = {2: "twenty", 
            3: "thirty", 
            4: "forty", 
            5: "fifty", 
            6: "sixty", 
            7: "seventy", 
            8: "eighty", 
            9: "ninety"}

    
    if not 0 <= number <= 999999999999: 
        raise ValueError("input out of range")

    if number == 0: 
        return "zero"

    def translate_chunk(value):
        """
        Fonction qui va transformer un bloc de 3 chiffres en mots
        """
        words = []
        hundreds = value // 100 
        if hundreds > 0: 
            words.append(f"{num_ones[hundreds]} hundred")

        remainder = value % 100
        if remainder > 0: 
            if remainder < 10: 
                words.append(num_ones[remainder])
            elif remainder < 20: 
                words.append(num_teens[remainder])
            else: 
                tens = remainder // 10
                units = remainder % 10
                if units > 0:
                    words.append(f"{num_tens[tens]}-{num_ones[units]}")
                else:
                    words.append(num_tens[tens])
        return " ".join(words)
        

    chunks = ["", "thousand", "million", "billion"]
    results = []
    chunk_index = 0

    #Boucle qui va prendre un bloc de trois par bloc de trois, le traduire grâce à la fonction translate_chunk, puis ajouter mille, million et millard au bloque correspondant
    while number > 0: 
        block = number % 1000 
        if block > 0: 
            text_block = translate_chunk(block)
            if chunks[chunk_index]:
                text_block += f" {chunks[chunk_index]}"
            #On insert toujours le nouveau bloque au début pour suivre la logique des nombres
            results.insert(0, text_block)

        number = number // 1000
        chunk_index += 1

    return " ".join(results)
            
            
        

    
    
    
