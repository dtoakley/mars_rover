
from .coordinates import Coordinates


class Plateau:

    def __init__(self, top_right_coordinates: Coordinates):
        self.bottom_left_coordinates = Coordinates(0, 0)
        self.top_right_coordinates = top_right_coordinates

    def has_within_bounds(self, coordinates: Coordinates) -> bool:
        return self._is_within_bottom_left_coordinates(coordinates) \
               and self._is_within_top_right_coordinates(coordinates)

    def _is_within_bottom_left_coordinates(self, coordinates: Coordinates) -> bool:
        return coordinates.x_coordinate >= self.bottom_left_coordinates.x_coordinate \
               and coordinates.y_coordinate >= self.bottom_left_coordinates.y_coordinate

    def _is_within_top_right_coordinates(self, coordinates: Coordinates) -> bool:
        return coordinates.x_coordinate <= self.top_right_coordinates.x_coordinate \
               and coordinates.y_coordinate <= self.top_right_coordinates.y_coordinate
