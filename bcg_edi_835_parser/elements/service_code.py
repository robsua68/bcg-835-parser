from bcg_edi_835_parser.elements import Element
from bcg_edi_835_parser.elements.utilities import split_element

class ServiceCode(Element):
    """Service Code"""

    def parser(self, value: str) -> str:
        value = split_element(value)
        _, code, *_ = value
        return code