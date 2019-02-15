from .base_command import BaseCommand
from mars_rover import MarsRover


class MoveCommand(BaseCommand):

    def execute(self, mars_rover: MarsRover) -> None:
        mars_rover.move()
