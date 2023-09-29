""" Dollars """
from typing import Optional

from Rsa_835_Parser.elements import Element

class Dollars(Element):
    """ Dollars Class """

    def parser(self, value: str) -> Optional[float]:
        if value != "":
            return float(value)
