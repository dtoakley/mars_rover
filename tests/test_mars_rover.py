import unittest

from mars_rover import MarsRover
from mars_rover.location import Plateau, Direction, Coordinates


class TestMarsRover(unittest.TestCase):

    def setUp(self):
        self.starting_coordinates = Coordinates(3, 3)
        self.plateau = Plateau(self.starting_coordinates)
        self.direction = Direction(Direction.NORTH)
        self.mars_rover = MarsRover(self.plateau, self.direction, self.starting_coordinates)

    def test_mars_rover_returns_current_location_as_string(self):
        # when
        current_location_string = self.mars_rover.get_current_location()

        # then
        self.assertEqual('3 3 N', current_location_string)

    def test_mars_rover_can_turn_left(self):
        # when
        self.mars_rover.turn_left()

        # then
        self.assertEqual('3 3 W', self.mars_rover.get_current_location())

    def test_mars_rover_can_turn_right(self):
        # when
        self.mars_rover.turn_right()

        # then
        self.assertEqual('3 3 E', self.mars_rover.get_current_location())

    def test_mars_rover_can_turn_move(self):
        # when
        self.mars_rover.move()

        # then
        self.assertEqual('4 3 N', self.mars_rover.get_current_location())
