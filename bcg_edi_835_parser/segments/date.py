""" Date segment """
from bcg_edi_835_parser.elements.identifier import Identifier
from bcg_edi_835_parser.elements.date import Date as DateElement
from bcg_edi_835_parser.elements.date_qualifier import DateQualifier
from bcg_edi_835_parser.segments.utilities import split_segment

class Date:
    """Date (DTM) segment Class"""

    identification = "DTM"

    identifier = Identifier()
    date = DateElement()
    qualifier = DateQualifier()

    def __init__(self, segment: str):
        self.segment = segment
        segment = split_segment(segment)

        self.identifier = segment[0]
        self.qualifier = segment[1]
        self.date = segment[2]

    def __repr__(self) -> str:
        return "\n".join(str(item) for item in self.__dict__.items())


if __name__ == "__main__":
    pass
