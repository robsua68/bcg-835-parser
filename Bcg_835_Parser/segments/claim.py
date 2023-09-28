""" Claim Segment """

# Local imports
from Bcg_835_Parser.elements.identifier import Identifier
from Bcg_835_Parser.elements.claim_status import ClaimStatus
from Bcg_835_Parser.elements.dollars import Dollars
from Bcg_835_Parser.segments.utilities import split_segment

class Claim:
    """Claim (CLP) segment Class"""

    identification = "CLP"

    identifier = Identifier()
    status = ClaimStatus()
    charge_amount = Dollars()
    paid_amount = Dollars()
    claim_number: str = None

    def __init__(self, segment: str):
        self.segment = segment
        segment = split_segment(segment)

        self.identifier = segment[0]
        self.marker = segment[1]
        self.status = segment[2]
        self.charge_amount = segment[3]
        self.paid_amount = segment[4]
        self.claim_number = segment[6]

    def __repr__(self) -> str:
        return "\n".join(str(item) for item in self.__dict__.items())


if __name__ == "__main__":
    pass
