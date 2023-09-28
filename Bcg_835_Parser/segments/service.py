""" Service segment """
from Bcg_835_Parser.elements.identifier import Identifier
from Bcg_835_Parser.elements.dollars import Dollars
from Bcg_835_Parser.elements.service_code import ServiceCode
from Bcg_835_Parser.elements.service_qualifier import ServiceQualifier
from Bcg_835_Parser.elements.service_modifier import ServiceModifier
from Bcg_835_Parser.elements.integer import Integer
from Bcg_835_Parser.segments.utilities import split_segment, get_element


class Service:
    """Service segment Class"""

    identification = "SVC"

    identifier = Identifier()
    charge_amount = Dollars()
    paid_amount = Dollars()
    code = ServiceCode()
    qualifier = ServiceQualifier()
    modifier = ServiceModifier()
    allowed_units = Integer()
    billed_units = Integer()

    def __init__(self, segment: str):
        self.segment = segment
        segment = split_segment(segment)

        self.identifier = segment[0]
        self.code = segment[1]
        self.qualifier = segment[1]
        self.modifier = segment[1]
        self.charge_amount = segment[2]
        self.paid_amount = segment[3]

        # assume unit count of one if unit not provided
        default = 0 if self.paid_amount == 0 else 1
        self.allowed_units = get_element(segment, 5, default=default)

        self.billed_units = get_element(segment, 7, default=self.allowed_units)

    def __repr__(self):
        return "\n".join(str(item) for item in self.__dict__.items())


# end Class Service

if __name__ == "__main__":
    pass
# end if __name__ == '__main__'

# end of file
