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
        new_coordinates = self.coordinates.new_coordinates_for_steps(*self.direction.steps_for_move())

        if self.plateau.has_within_bounds(new_coordinates):
            self.coordinates = new_coordinates

    def run(self, command_string: str) -> None:
        from .parser import StringCommandParser
        mars_rover_commands = StringCommandParser(command_string).get_commands()

        for command in mars_rover_commands:
            command.execute(self)
