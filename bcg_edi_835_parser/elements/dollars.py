""" Dollars """
from typing import Optional

from Bcg_Edi_835_Parser.elements import Element

class Dollars(Element):
    """ Dollars Class """

    def parser(self, value: str) -> Optional[float]:
        if value != "":
            return float(value)
