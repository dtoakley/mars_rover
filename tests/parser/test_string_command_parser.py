from mars_rover.parser import StringCommandParser
from mars_rover.commands import TurnLeftCommand, TurnRightCommand, MoveCommand


class TestStringCommandParser:

    def test_string_l_maps_to_left_command(self):
        # given
        parser = StringCommandParser('L')

        # when
        commands = parser.get_commands()

        # then
        assert len(commands) == 1
        assert isinstance(commands[0], TurnLeftCommand)

    def test_string_r_maps_to_left_command(self):
        # given
        parser = StringCommandParser('R')

        # when
        commands = parser.get_commands()

        # then
        assert len(commands) == 1
        assert isinstance(commands[0], TurnRightCommand)

    def test_string_m_maps_to_left_command(self):
        # given
        parser = StringCommandParser('M')

        # when
        commands = parser.get_commands()

        # then
        assert len(commands) == 1
        assert isinstance(commands[0], MoveCommand)

    def test_string_create_commands(self):
        # given
        parser = StringCommandParser('LRM')

        # when
        commands = parser.get_commands()

        # then
        assert len(commands) == 3
        assert isinstance(commands[0], TurnLeftCommand)
        assert isinstance(commands[1], TurnRightCommand)
        assert isinstance(commands[2], MoveCommand)
