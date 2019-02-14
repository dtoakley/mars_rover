
from .location import Plateau, Direction, Coordinates


class MarsRover:

    def __init__(self, plateau: Plateau, direction: Direction, coordinates: Coordinates):
        self.plateau = plateau
        self.direction = direction
        self.coordinates = coordinates

    def get_current_location(self):
        return '{} {}'.format(self.coordinates, self.direction)

    def turn_left(self):
        self.direction.left()

    def turn_right(self):
        self.direction.right()

    def move(self):
        self.coordinates.change(*self.direction.steps_for_move())
