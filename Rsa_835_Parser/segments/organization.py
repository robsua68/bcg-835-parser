""" Organization segment """
from Rsa_835_Parser.elements.identifier import Identifier
from Rsa_835_Parser.elements.organization_type import OrganizationType
from Rsa_835_Parser.segments.utilities import split_segment


class Organization:
    """Organization (N1) segment Class"""

    identification = "N1"

    identifier = Identifier()
    type = OrganizationType()

    def __init__(self, segment: str):
        self.segment = segment
        segment = split_segment(segment)

        self.identifier = segment[0]
        self.type = segment[1]
        self.name = segment[2]

    def __repr__(self) -> str:
        return "\n".join(str(item) for item in self.__dict__.items())


if __name__ == "__main__":
    pass
