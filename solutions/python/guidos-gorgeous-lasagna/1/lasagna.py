"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://wikipedia.org
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers): 
    """Calculate the preparation time based on the number of layers.

    Parameters:
        number_of_layers (int): The number of layers added to the lasagna.

    Returns:
        int: Total preparation time (in minutes).
    """
    return number_of_layers * PREPARATION_TIME
        

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total elapsed cooking time (preparation + baking).

    Parameters:
        number_of_layers (int): The number of layers in the lasagna.
        elapsed_bake_time (int): The number of minutes the lasagna has been baking.

    Returns:
        int: Total elapsed minutes.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time

