"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    Parameters:
        items (list): Items to create an inventory from.

    Returns:
        dict: The inventory dictionary.
    """
    invetory = {}

    #Pour chaque valeur de la liste
    for value in items:
        #On compte le nombre de fois qu'il s'y trouve
        amount = items.count(value)
        #On l'enregistre dans le dictionnaire
        invetory[value] = amount
        
    return invetory

def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    Parameters:
        inventory (dict): Dictionary of existing inventory.
        items (list): List of items to update the inventory with.

    Returns:
        dict: The inventory updated with the new items.
    """
    for article in items: 
        if article not in inventory: 
            inventory[article] = 1
        else: 
            inventory[article] += 1

    return inventory

def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    Parameters:
        inventory (dict): Inventory dictionary.
        items (list): List of items to decrement from the inventory.

    Returns:
        dict: Updated inventory with items decremented.
    """
    for article in items: 
        if article in inventory:
            inventory[article] -= 1

            #Si l'article devient négatif, on le bloque à 0
            if inventory[article] < 0: 
                inventory[article] = 0
            
    return inventory
 

def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    Parameters:
        inventory (dict): Inventory dictionary.
        item (str): Item to remove from the inventory.

    Returns:
        dict: Updated inventory with item removed. Current inventory if item does not match.
    """

    if item in inventory:
        inventory.pop(item)

    return inventory

def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    Parameters:
        inventory (dict): An inventory dictionary.

    Returns:
        list[tuple]: List of key, value tuples from the inventory dictionary.
    """
    result = []
    for article, quantity in inventory.items():
        if quantity > 0: 
            result.append((article, quantity))
    return result
        
