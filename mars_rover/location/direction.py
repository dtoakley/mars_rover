
from enum import Enum


class Direction(Enum):
    NORTH = 'N'
    SOUTH = 'S'
    EAST = 'E'
    WEST = 'W'

    def __init__(self, heading: str):
        self.heading = heading

    def __str__(self):
        return self.heading



