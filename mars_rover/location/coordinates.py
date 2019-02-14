

class Coordinates:

    def __init__(self, x_coordinate: int, y_coordinate: int):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def __str__(self):
        return '{} {}'.format(self.x_coordinate, self.y_coordinate)

    def change(self, x_coordinate: int, y_coordinate: int):
        self.x_coordinate += x_coordinate
        self.y_coordinate += y_coordinate
