def is_isogram(phrase):
    letters = [caractere for caractere in phrase.lower() if caractere.isalpha()]
    letters_set = set(letters)

    return len(letters) == len(letters_set)
        
