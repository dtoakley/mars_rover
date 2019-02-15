from .base_command import BaseCommand
from mars_rover import MarsRover


class TurnLeftCommand(BaseCommand):

    def execute(self, mars_rover: MarsRover) -> None:
        mars_rover.turn_left()
