
from .coordinates import Coordinates


class Plateau:

    def __init__(self, top_right_coordinates: Coordinates):
        self.bottom_left_coordinates = Coordinates(0, 0)
        self.top_right_coordinates = top_right_coordinates
