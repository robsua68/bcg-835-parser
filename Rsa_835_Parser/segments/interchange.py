""" Interchange Segment """

# Local Imports
from Rsa_835_Parser.elements.authorization_information_qualifier import (
    AuthorizationInformationQualifier,
)
from Rsa_835_Parser.elements.organization import Organization
from Rsa_835_Parser.elements.date import Date
from Rsa_835_Parser.elements.identifier import Identifier
from Rsa_835_Parser.segments.utilities import split_segment


class Interchange:
    # Iterchange Segment Class Definition
    """Interchange Segment Class"""
    identification = "ISA"

    identifier = Identifier()
    autorization_information_qualifier = AuthorizationInformationQualifier()
    sender = Organization()
    receiver = Organization()
    transimission_date = Date()

    def __init__(self, segment: str):
        self.segment = segment
        segment = split_segment(segment)

        self.identifier = segment[0]
        self.autorization_information_qualifier = segment[1]
        self.sender = segment[6]
        self.receiver = segment[8]
        self.transimission_date = segment[9] + segment[10]

    def __repr__(self) -> str:
        return "\n".join(str(item) for item in self.__dict__.items())


if __name__ == "__main__":
    pass
