"""
Exercice Python: Circular buffer
"""
from collections import deque

class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.

    message: explanation of the error.

    """
    def __init__(self, message):
        super().__init__(message)


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.

    message: explanation of the error.

    """
    def __init__(self, message):
        super().__init__(message)


class CircularBuffer:
    """
    Représentation d'un tampon circulaire de taille fixe
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = deque(maxlen = capacity)

    def read(self):
        """
        Fonction pour lire le tampon
        """
        if len(self.buffer) == 0: 
            raise BufferEmptyException("Circular buffer is empty")
        return self.buffer.popleft()

    def write(self, data):
        """
        Fonction pour écrire le tampon
        """
        if len(self.buffer) == self.capacity: 
            raise BufferFullException("Circular buffer is full")
        self.buffer.append(data)

    def overwrite(self, data):
        """
        Fonction pour surécrire sur le tampon (donc écrire si ce n'est pas vide et supprimer et écrire si c'est rempli)
        """
        self.buffer.append(data)

    def clear(self):
        """
        Fonction pour tout nettoyer
        """
        self.buffer.clear()
