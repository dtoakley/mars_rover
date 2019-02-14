import pytest

from mars_rover.location import Direction


class TestDirection:

    @pytest.mark.parametrize('starting_direction,final_direction', [
        (Direction.NORTH, Direction.WEST),
        (Direction.SOUTH, Direction.EAST),
        (Direction.EAST, Direction.NORTH),
        (Direction.WEST, Direction.SOUTH),
    ])
    def test_left(self, starting_direction, final_direction):

        # given
        direction = Direction(starting_direction)

        # when
        direction.left()

        # then
        assert direction.heading == final_direction

    @pytest.mark.parametrize('starting_direction,final_direction', [
        (Direction.NORTH, Direction.EAST),
        (Direction.SOUTH, Direction.WEST),
        (Direction.EAST, Direction.SOUTH),
        (Direction.WEST, Direction.NORTH),
    ])
    def test_right(self, starting_direction, final_direction):

        # given
        direction = Direction(starting_direction)

        # when
        direction.right()

        # then
        assert direction.heading == final_direction

    @pytest.mark.parametrize('starting_direction,expected_steps', [
        (Direction.NORTH, (1, 0)),
        (Direction.SOUTH, (-1, 0)),
        (Direction.EAST, (0, 1)),
        (Direction.WEST, (0, -1)),
    ])
    def test_steps_for_move(self, starting_direction, expected_steps):
        # given
        direction = Direction(starting_direction)

        # when
        steps = direction.steps_for_move()

        # then
        assert steps == expected_steps
