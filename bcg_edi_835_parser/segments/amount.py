""" Amount (AMT) segment """
from Bcg_Edi_835_Parser.elements.identifier import Identifier
from Bcg_Edi_835_Parser.elements.dollars import Dollars
from Bcg_Edi_835_Parser.elements.amount_qualifier import AmountQualifier
from Bcg_Edi_835_Parser.segments.utilities import split_segment


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
