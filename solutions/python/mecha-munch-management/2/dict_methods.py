"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    Parameters:
        current_cart (dict): The current shopping cart.
        items_to_add (iterable): The items to add to the cart.

    Returns:
        dict: The updated user cart dictionary.
    """
    for item in items_to_add: 
        current_cart[item] = current_cart.get(item, 0) + 1
        
    return current_cart


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    Parameters:
        notes (iterable): Group of items to add to cart.

    Returns:
        dict: A user shopping cart dictionary.
    """
    return dict.fromkeys(notes, 1)


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    Parameters:
        ideas (dict): The "recipe ideas" dict.
        recipe_updates (iterable): Updates for the ideas section.

    Returns:
        dict: The updated "recipe ideas" dict.
    """
    ideas.update(recipe_updates)
    return ideas


def sort_entries(cart):
    """Sort a user's shopping cart in alphabetical order.

    Parameters:
        cart (dict): A user's shopping cart dictionary.

    Returns:
        dict: A user's shopping cart sorted in alphabetical order.
    """

    return dict(sorted(cart.items()))


def send_to_store(cart, aisle_mapping):
    """Combine user's order to aisle and refrigeration information.

    Parameters:
        cart (dict): The user's shopping cart dictionary.
        aisle_mapping (dict): The aisle and refrigeration information dictionary.

    Returns:
        dict: The fulfillment dictionary ready to send to store.
    """
    result = {}
    
    for item, quantity in cart.items(): 
        # Sécurité : évite le plantage si l'article n'est pas référencé
        shop_info = aisle_mapping.get(item, ["Unknown Aisle", "Unknown Temp"])
        result[item] = [quantity] + shop_info

    # Trie par ordre alphabétique inversé
    sorted_items = sorted(
        result.items(), 
        key=lambda x: x[0], reverse=True)  # Trie selon le nom 

    return dict(sorted_items)


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    Parameters:
        fulfillment cart (dict): The fulfillment cart to send to store.
        store_inventory (dict): The stores available inventory.

    Returns:
        dict: The store_inventory updated.
    """
    for item, cart_details in fulfillment_cart.items(): 
        quantity_ordered = cart_details[0]

        if item in store_inventory: 
            store_inventory[item][0] -= quantity_ordered

            if store_inventory[item][0] <=0:
                store_inventory[item][0] = "Out of Stock"
                print(f"Rupture de stock pour l'article : {item}")

    return store_inventory
        
