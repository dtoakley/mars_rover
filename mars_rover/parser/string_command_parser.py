from typing import List

from mars_rover.commands import TurnLeftCommand, TurnRightCommand, MoveCommand


class StringCommandParser:

    COMMAND_MAPPING = {
        'L': TurnLeftCommand(),
        'R': TurnRightCommand(),
        'M': MoveCommand(),
    }

    def __init__(self, command_string: str) -> None:
        self.command_string = command_string

    def get_commands(self) -> List:
        commands = []
        for character in self.command_string:
            commands.append(self.COMMAND_MAPPING.get(character))

        return commands
