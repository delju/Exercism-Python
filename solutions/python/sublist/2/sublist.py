"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = "SUBLIST"
SUPERLIST = "SUPERLIST"
EQUAL = "EQUAL"
UNEQUAL = "UNEQUAL"

def is_a_sublist(small, large): 
    if not small: 
        return True
        
    len_small = len(small)
    len_large = len(large)

    return any(large[i : i + len_small] == small for i in range(len_large - len_small + 1))  
    
def sublist(list_one, list_two):

    
    if list_one == list_two: 
        return EQUAL 

    if len(list_one) > len(list_two) and is_a_sublist(list_two, list_one): 
        return SUPERLIST

    if len(list_one) < len(list_two) and is_a_sublist(list_one, list_two): 
        return SUBLIST

    return UNEQUAL
        
    
