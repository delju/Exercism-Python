"""
Exercice Python Anagram. Vérifer si un mot candidat est un anagram du mot cible.
"""

def find_anagrams(word, candidates):
    """
    Fonction permettant de nettoyer les mots, et de vérifer que les lettres sont les mêmes mais que le mot est différent. 
    """
    letters = sorted(word.lower())

    anagram = []

    for word_candidate in candidates:
        
        letters_candidate = sorted(word_candidate.lower())
    
        if word_candidate.lower() != word.lower() and letters_candidate == letters: 
            anagram.append(word_candidate)

    return anagram
            