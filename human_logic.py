import random
import datetime

import objects


def get_random_player():
    """
    Creates a Player object with a random map
    :return: Player
    """
    player = objects.Player()
    ships = objects.get_list_of_ships()

    j = 0
    for index,ship in enumerate(ships):
        i = 0
        j += 1

        while not __is_added(player, ship, index):
            i += 1

    return player

def __is_added(player, ship, index):
    """
    :param player: Player - an object Player
    :orientation: decide orientation as the request of project
    :param ship: Ship - a ship that has to be tried to put on the map of Player
    :return: True if the given ship has been put successfully
    """
    random.seed(datetime.datetime.now().microsecond)
    if index % 2 ==1 :
        orientation = 1
    else:
        orientation = 2
    if orientation == objects.HORIZONTAL:
        x = random.randint(1, 9 - ship)
        y = random.randint(1, 8)
    else:
        x = random.randint(1, 8)
        y = random.randint(1, 9 - ship)

    return player.add_ship(objects.Ship(ship, orientation, x, y))
