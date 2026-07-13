"""
Exercice python RNA Transcription. Donc remplacer des lettres par d'autres qui correspondent.
"""

def to_rna(dna_strand):
    """
    Utilisation de la fonction str.maketrans qui génère un dictionnaire automatiquement
    """
    text_translate = str.maketrans("GCTA", "CGAU")
    return dna_strand.translate(text_translate)

