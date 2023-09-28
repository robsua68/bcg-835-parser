""" Service Modifier """
from typing import Optional

from bcg_edi_835_parser.elements import Element
from bcg_edi_835_parser.elements.utilities import split_element

class ServiceModifier(Element):
    """Service Modifier"""

    def parser(self, value: str) -> Optional[str]:
        value = split_element(value)
        if len(value) > 2:
            return value[2]
