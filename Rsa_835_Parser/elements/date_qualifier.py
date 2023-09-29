""" Date Qualifier """
from Rsa_835_Parser.elements import Element

# https://ediacademy.com/blog/x12-date-time-qualifiers/
date_qualifiers = {
    "050": "received",
    "150": "service period start",
    "151": "service period end",
    "472": "service",
    "232": "claim statement period start",
    "233": "claim statement period end",
}


class DateQualifier(Element):
    """Date Qualifier"""

    def parser(self, value: str) -> str:
        return date_qualifiers.get(value, value)
