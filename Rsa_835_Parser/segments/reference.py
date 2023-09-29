""" Reference (REF) segment """
from Rsa_835_Parser.elements.identifier import Identifier
from Rsa_835_Parser.elements.reference_qualifier import ReferenceQualifier
from Rsa_835_Parser.segments.utilities import split_segment


class Reference:
    """Reference (REF) segment Class"""

    identification = "REF"

    identifier = Identifier()
    qualifier = ReferenceQualifier()

    def __init__(self, segment: str):
        self.segment = segment
        segment = split_segment(segment)

        self.identifier = segment[0]
        self.qualifier = segment[1]
        self.value = segment[2]

    def __repr__(self) -> str:
        return "\n".join(str(item) for item in self.__dict__.items())

    def __str__(self) -> str:
        return f"{self.identifier}: {self.value}"


if __name__ == "__main__":
    pass
