from mars_rover.parser import StringLocationsParser


class TestStringLocationParser:

    def test_location_string_parses_only_coordinates(self):
        # given
        string_location_parser = StringLocationsParser('0 0')

        # when
        coordinates, heading = string_location_parser.get_coordinates_and_heading()

        # then
        assert coordinates == (0, 0)
        assert heading is None

    def test_location_string_parses_coordinates_and_heading(self):
        # given
        string_location_parser = StringLocationsParser('0 0 N')

        # when
        coordinates, heading = string_location_parser.get_coordinates_and_heading()

        # then
        assert coordinates == (0, 0)
        assert heading == 'N'
