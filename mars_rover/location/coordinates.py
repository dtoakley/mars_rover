

class Coordinates:

    def __init__(self, x_coordinate: int, y_coordinate: int):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def __str__(self):
        return '{} {}'.format(self.x_coordinate, self.y_coordinate)

    def new_coordinates_for_steps(self, step_in_x_direction: int, step_in_y_direction: int):
        return Coordinates(self.x_coordinate + step_in_x_direction, self.y_coordinate + step_in_y_direction)
