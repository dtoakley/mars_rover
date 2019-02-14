import pytest

from mars_rover.location import Coordinates


class TestCoordinates:

    @pytest.mark.parametrize('steps,expected_x_coordinate, expected_y_coordinate', [
        ((1, 0), 4, 3),
        ((-1, 0), 2, 3),
        ((0, 1), 3, 4),
        ((0, -1), 3, 2),
    ])
    def test_new_coordinates_for_steps(self, steps, expected_x_coordinate, expected_y_coordinate):
        # given
        coordinates = Coordinates(3, 3)

        # when
        new_coordinate = coordinates.new_coordinates_for_steps(*steps)

        # then
        assert new_coordinate.x_coordinate == expected_x_coordinate
        assert new_coordinate.y_coordinate == expected_y_coordinate
