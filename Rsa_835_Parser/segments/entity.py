""" Entity (NM1) segment """

# Local imports
from rsa_835_parser.elements.identifier import Identifier
from rsa_835_parser.elements.entity_code import EntityCode
from rsa_835_parser.elements.entity_type import EntityType
from rsa_835_parser.elements.identification_code_qualifier import (
    IdentificationCodeQualifier,
)
from rsa_835_parser.segments.utilities import split_segment, get_element

class Entity:
    """Entity Class segment"""

    identification = "NM1"

    identifier = Identifier()
    entity_code = EntityCode()
    type = EntityType()
    identification_code_qualifier = IdentificationCodeQualifier()

    def __init__(self, segment: str):
        self.segment = segment
        segment = split_segment(segment)

        self.identifier = segment[0]
        self.entity = segment[1]
        self.type = segment[2]
        self.last_name = segment[3]
        self.first_name = get_element(segment, 4)
        self.identification_code_qualifier = get_element(segment, 8)
        self.identification_code = get_element(segment, 9)

    def __repr__(self) -> str:
        return "\n".join(str(item) for item in self.__dict__.items())

    # This property has been changed from the original code.
    # Patient Name = Last Name, First Name in Uppercase
    @property
    def name(self) -> str:
        """return the patient name"""
        return f"{self.last_name}, {self.first_name}".upper()


# End-of-Class (Entity)
if __name__ == "__main__":
    pass

# End-of-file (EOF)
