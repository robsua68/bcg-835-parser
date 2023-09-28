""" Address segment """
from Bcg_Edi_835_Parser.elements.identifier import Identifier
from Bcg_Edi_835_Parser.segments.utilities import split_segment


class Address:
    """Address (N3) segment Class"""

    identification = "N3"

    identifier = Identifier()

    def __init__(self, segment: str):
        self.segment = segment
        segment = split_segment(segment)

        self.identifier = segment[0]
        self.address = segment[1]

    def __repr__(self) -> str:
        return "\n".join(str(item) for item in self.__dict__.items())


if __name__ == "__main__":
    pass
