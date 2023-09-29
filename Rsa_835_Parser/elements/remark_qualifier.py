""" Remark Qualifier """
from Rsa_835_Parser.elements import Element, Code

remark_qualifiers = {"HE": "claim payment"}

class RemarkQualifier(Element):
    """Remark Qualifier"""

    def parser(self, value: str) -> Code:
        description = remark_qualifiers.get(value, None)
        return Code(value, description)
