""" Service Qualifier """
from bcg_edi_835_parser.elements import Element
from bcg_edi_835_parser.elements.utilities import split_element


class ServiceQualifier(Element):
    """Service Qualifier"""

    def parser(self, value: str) -> str:
        value = split_element(value)
        qualifier, *_ = value
        return qualifier
