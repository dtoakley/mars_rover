
from .location import Plateau, Direction, Coordinates


class MarsRover:

    def __init__(self, plateau: Plateau, direction: Direction, coordinates: Coordinates):
        self.plateau = plateau
        self.direction = direction
        self.coordinates = coordinates

    def get_current_location(self):
        return '{} {}'.format(self.coordinates, self.direction)
