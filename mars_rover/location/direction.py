
class Direction:
    NORTH = 'N'
    SOUTH = 'S'
    EAST = 'E'
    WEST = 'W'

    LEFT = 'L'
    RIGHT = 'R'

    HEADING_MAPPING = {
        NORTH: {
            LEFT: WEST,
            RIGHT: EAST,
        },
        SOUTH: {
            LEFT: EAST,
            RIGHT: WEST,
        },
        EAST: {
            LEFT: NORTH,
            RIGHT: SOUTH,
        },
        WEST: {
            LEFT: SOUTH,
            RIGHT: NORTH,
        }
    }

    STEP_SIZE_MAPPING = {
        NORTH: (1, 0),
        SOUTH: (-1, 0),
        EAST: (0, 1),
        WEST: (0, -1),
    }

    def __init__(self, heading: str):
        self.heading = heading

    def __str__(self):
        return self.heading

    def left(self):
        self.heading = self.HEADING_MAPPING[self.heading][self.LEFT]

    def right(self):
        self.heading = self.HEADING_MAPPING[self.heading][self.RIGHT]

    def steps_for_move(self):
        return self.STEP_SIZE_MAPPING[self.heading]

