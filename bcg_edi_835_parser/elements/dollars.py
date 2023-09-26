from typing import Optional

from bcg_edi_835_parser.elements import Element

class Dollars(Element):
    """Dollars"""
    
    def parser(self, value: str) -> Optional[float]:
        if value != '':
            return float(value)
