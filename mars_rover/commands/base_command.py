from abc import ABC, abstractmethod

from mars_rover import MarsRover


class BaseCommand(ABC):

    @abstractmethod
    def execute(self, mars_rover: MarsRover) -> None:
        pass
