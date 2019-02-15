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
        assert '0 1 N' == self.mars_rover.get_current_location()

    def test_mars_rover_wont_move_off_plateau(self):
        # given
        self.mars_rover.turn_left()

        # when
        self.mars_rover.move()

        # then
        assert '0 0 W' == self.mars_rover.get_current_location()

    def test_can_run_command_to_rotate_left(self):
        # when
        self.mars_rover.run('L')

        # then
        assert '0 0 W' == self.mars_rover.get_current_location()

    def test_can_run_command_to_rotate_right(self):
        # when
        self.mars_rover.run('R')

        # then
        assert '0 0 E' == self.mars_rover.get_current_location()

    def test_can_run_command_to_move(self):
        # when
        self.mars_rover.run('M')

        # then
        assert '0 1 N' == self.mars_rover.get_current_location()

    @pytest.mark.parametrize('mars_rover_coordinates,mars_rover_direction,command_string,expected_output', [
        ((1, 2), Direction.NORTH, 'LMLMLMLMM', '1 3 N'),
        ((3, 3), Direction.EAST, 'MMRMMRMRRM', '5 1 E'),
    ])
    def test_mars_rover_run(self, mars_rover_coordinates, mars_rover_direction, command_string, expected_output):
        # given
        direction = Direction(mars_rover_direction)
        mars_rover = MarsRover(self.plateau, direction, Coordinates(*mars_rover_coordinates))

        # when
        mars_rover.run(command_string)

        # then
        assert expected_output == mars_rover.get_current_location()
