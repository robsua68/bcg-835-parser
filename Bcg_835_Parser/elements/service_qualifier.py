""" Service Qualifier """
from Bcg_835_Parser.elements import Element
from Bcg_835_Parser.elements.utilities import split_element


class ServiceQualifier(Element):
    """Service Qualifier"""

    def parser(self, value: str) -> str:
        value = split_element(value)
        qualifier, *_ = value
        return qualifier
