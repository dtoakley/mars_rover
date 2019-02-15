

class StringLocationsParser:

    def __init__(self, location_string: str) -> None:
        self.location_string = ''.join(location_string.split(' '))

    def get_coordinates_and_heading(self):
        heading = self.location_string[-1:] if len(self.location_string) > 2 else None
        coordinates = tuple(int(character) for character in self.location_string if character.isdigit())
        return coordinates, heading

