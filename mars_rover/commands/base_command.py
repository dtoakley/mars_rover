from abc import ABC

from mars_rover import MarsRover


class BaseCommand(ABC):

    def execute(self, mars_rover) -> None:
        pass
