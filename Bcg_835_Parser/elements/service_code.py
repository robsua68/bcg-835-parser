"""Service Code"""
from Bcg_835_Parser.elements import Element
from Bcg_835_Parser.elements.utilities import split_element

class ServiceCode(Element):
    """Service Code"""

    def parser(self, value: str) -> str:
        value = split_element(value)
        _, code, *_ = value
        return code
