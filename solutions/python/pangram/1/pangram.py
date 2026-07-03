def is_pangram(sentence):
    # On ne garde que les caractères qui sont des lettres
    letters = {caractere for caractere in sentence.lower() if caractere.isalpha()}

    return len(letters) == 26 
      

    
