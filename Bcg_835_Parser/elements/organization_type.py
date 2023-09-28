""" Organization Type """
from Bcg_835_Parser.elements import Element

organization_types = {
    "PE": "payee",
    "PR": "payer",
}

class OrganizationType(Element):
    """Organization Type Class"""

    def parser(self, value: str) -> str:
        value = value.strip()
        return organization_types.get(value, value)
