""" Organization Element """
from Bcg_Edi_835_Parser.elements import Element

organizations = {"AV09311993": "Availity", "ZIRMED": "Zirmed"}


class Organization(Element):
    """Organization Class"""

    def parser(self, value: str) -> str:
        value = value.strip()
        return organizations.get(value, value)
