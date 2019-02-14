import unittest

from mars_rover import MarsRover
from mars_rover.location import Plateau, Direction, Coordinates


class TestMarsRover(unittest.TestCase):

    def test_mars_rover_returns_current_location_as_string(self):
        # given
        starting_coordinates = Coordinates(3, 3)
        plateau = Plateau(starting_coordinates)
        direction = Direction(Direction.NORTH)

        # when
        mars_rover = MarsRover(plateau, direction, starting_coordinates)
        current_location_string = mars_rover.get_current_location()

        # then
        self.assertEqual('3 3 N', current_location_string)
