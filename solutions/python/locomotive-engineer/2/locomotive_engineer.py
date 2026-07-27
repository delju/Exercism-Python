"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    """Return a list of wagons, given an arbitrary amount of wagon numbers.

    Parameters:
        An arbitrary number of wagon numbers, unpacked.

    Returns:
        list: A list of wagon numbers.
    """
    return list(args)



def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    Parameters:
        each_wagons_id (list[int]): The list of wagons.
        missing_wagons (list[int]): The list of missing wagons.

    Returns:
        list[int]: The corrected list of wagons.
    """
    wagon_a, wagon_b, wagon_c, *rest = each_wagons_id
    return [wagon_c, *missing_wagons, *rest, wagon_a, wagon_b]



def add_missing_stops(route, **kwargs):
    """Add missing stops to route dict.

    Parameters:
        route (dict): The dict of routing information.
        (dict): An arbitrary number of stops.

    Returns:
        dict: The updated route dictionary.
    """
    #Je récupère les valeurs de la partie kwarg et je la mets dans une liste
    list_stop = list(kwargs.values())
    #j'ajoute la liste au dictionnaire avec stop comme clé.
    route["stops"] =list_stop

    return route

def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    Parameters:
        route (dict): The route information.
        more_route_information (dict): The extra route information.

    Returns:
        dict: The extended route information.
    """
    combined_road = {**route, **more_route_information}
    return combined_road


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    Parameters:
        wagons_rows (list[list[tuple]]): The list of rows of wagons.

    Returns:
        list[list[tuple]]: the list of rows of wagons.
    """
    return [list(line) for line in zip(*wagons_rows)]
