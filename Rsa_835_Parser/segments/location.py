""" Location (N4) segment """
from rsa_835_parser.elements.identifier import Identifier
from rsa_835_parser.segments.utilities import split_segment

class Location:
    """Location (N4) segment Class"""

    identification = "N4"

    identifier = Identifier()

    def __init__(self, segment: str):
        self.segment = segment
        segment = split_segment(segment)

        self.identifier = segment[0]
        self.city = segment[1]
        self.state = segment[2]
        self.zip = segment[3]

    def __repr__(self) -> str:
        return "\n".join(str(item) for item in self.__dict__.items())

# end Class Location

if __name__ == "__main__":
    pass
# end if __name__ == '__main__'

# end of file
