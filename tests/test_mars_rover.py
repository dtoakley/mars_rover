import pytest

from mars_rover import MarsRover
from mars_rover.location import Plateau, Direction, Coordinates


class TestMarsRover:

    @pytest.fixture(autouse=True)
    def set_up(self):
        self.plateau_coordinates = Coordinates(5, 5)
        self.plateau = Plateau(self.plateau_coordinates)
        self.direction = Direction(Direction.NORTH)
        self.mars_rover = MarsRover(self.plateau, self.direction, Coordinates(0, 0))

    def test_mars_rover_returns_current_location_as_string(self):
        # when
        current_location_string = self.mars_rover.get_current_location()

        # then
        assert '0 0 N' == current_location_string

    def test_mars_rover_can_turn_left(self):
        # when
        self.mars_rover.turn_left()

        # then
        assert '0 0 W' == self.mars_rover.get_current_location()

    def test_mars_rover_can_turn_right(self):
        # when
        self.mars_rover.turn_right()

        # then
        assert '0 0 E' == self.mars_rover.get_current_location()

    def test_mars_rover_can_turn_move(self):
        # when
        self.mars_rover.move()

        # then
        assert '1 0 N' == self.mars_rover.get_current_location()

    def test_mars_rover_wont_move_off_plateau(self):
        # given
        self.mars_rover.turn_left()

        # when
        self.mars_rover.move()

        # then
        assert '0 0 W' == self.mars_rover.get_current_location()

