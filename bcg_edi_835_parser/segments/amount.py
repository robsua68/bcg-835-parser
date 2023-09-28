""" Amount (AMT) segment """
from bcg_edi_835_parser.elements.identifier import Identifier
from bcg_edi_835_parser.elements.dollars import Dollars
from bcg_edi_835_parser.elements.amount_qualifier import AmountQualifier
from bcg_edi_835_parser.segments.utilities import split_segment


class Amount:
    """Amount (AMT) segment Class"""

    identification = "AMT"

    identifier = Identifier()
    qualifier = AmountQualifier()
    amount = Dollars()

    def __init__(self, segment: str):
        self.segment = segment
        segment = split_segment(segment)

        self.identifier = segment[0]
        self.qualifier = segment[1]
        self.amount = segment[2]

    def __repr__(self) -> str:
        return "\n".join(str(item) for item in self.__dict__.items())


if __name__ == "__main__":
    pass
