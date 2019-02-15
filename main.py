import os

from mars_rover.parser import StringLocationsParser
from mars_rover.location import Plateau, Direction, Coordinates
from mars_rover import MarsRover


class Application:

    def __init__(self):
        self.input_file = open(os.path.join(os.getcwd(), 'mars_rover/data/input.txt'), 'r')
        self.files_lines = self.input_file.read().splitlines()

    def process_input_file(self):

        plateau = self._get_plateau()

        mars_rover = self._get_mars_rover(plateau, 1)
        mars_rover.run(self.files_lines[2])
        print(mars_rover.get_current_location())

        mars_rover_2 = self._get_mars_rover(plateau, 3)
        mars_rover_2.run(self.files_lines[4])
        print(mars_rover_2.get_current_location())

    def _get_plateau(self):
        plateau_coordinates = StringLocationsParser(self.files_lines[0]).get_coordinates_and_heading()
        plateau_coordinates = Coordinates(*plateau_coordinates[0])

        return Plateau(plateau_coordinates)

    def _get_mars_rover(self, plateau: Plateau, line_number: int):
        mars_rover_coordinates, mars_rover_heading = StringLocationsParser(
             self.files_lines[line_number]
         ).get_coordinates_and_heading()
        return MarsRover(
            plateau,
            Direction(mars_rover_heading),
            Coordinates(*mars_rover_coordinates)
         )


if __name__ == '__main__':
    application = Application()
    application.process_input_file()


