""" Service Modifier """
from typing import Optional

from Bcg_Edi_835_Parser.elements import Element
from Bcg_Edi_835_Parser.elements.utilities import split_element

class ServiceModifier(Element):
    """Service Modifier"""

    def parser(self, value: str) -> Optional[str]:
        value = split_element(value)
        if len(value) > 2:
            return value[2]
