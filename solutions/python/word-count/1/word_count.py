"""
Exercice Python: Word count 
"""
import re

def count_words(sentence):
    """
    Fonction qui génére une liste des mots sur une phrase donnée, et le nombre de fois que le mot est utilisé.
    """
    #On nettoie la phrase avec l'expression régulière re, et en minuscule
    word_list = re.findall(r"[a-z0-9]+(?:\'[a-z0-9]+)?", sentence.lower())
                           
    word_count = {} 

    #Pour chaque mot dans la liste, on compte le nombre de fois qu'il est utilisé et on ajoute tout ça dans la liste
    for word in word_list: 

        amount = word_list.count(word)
        word_count[word] = amount

    return word_count
    