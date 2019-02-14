import pytest

from mars_rover.location import Coordinates, Plateau


class TestPlateau:

    @pytest.mark.parametrize('new_coordinates,within_bounds', [
        ((0, 0), True),
        ((3, 3), True),
        ((0, -1), False),
        ((-1, 0), False),
        ((6, 0), False),
        ((0, 6), False),
        ((6, 6), False),
    ])
    def test_has_within_bounds(self, new_coordinates, within_bounds):
        # given
        coordinates = Coordinates(5, 5)
        plateau = Plateau(coordinates)

        # when
        new_coordinates = Coordinates(*new_coordinates)

        # then
        assert plateau.has_within_bounds(new_coordinates) == within_bounds
