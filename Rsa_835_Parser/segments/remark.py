""" Remark (LQ) segment """
from Rsa_835_Parser.elements.identifier import Identifier
from Rsa_835_Parser.elements.remark_qualifier import RemarkQualifier
from Rsa_835_Parser.elements.remark_code import RemarkCode
from Rsa_835_Parser.segments.utilities import split_segment


class Remark:
    """Remark (LQ) segment Class"""

    identification = "LQ"

    identifier = Identifier()
    qualifier = RemarkQualifier()
    code = RemarkCode()

    def __init__(self, segment: str):
        self.segment = segment
        segment = split_segment(segment)

        self.identifier = segment[0]
        self.qualifier = segment[1]
        self.code = segment[2]

    def __repr__(self):
        return "\n".join(str(item) for item in self.__dict__.items())


# end Class Remark

if __name__ == "__main__":
    pass
# end if __name__ == '__main__'

# end of file
