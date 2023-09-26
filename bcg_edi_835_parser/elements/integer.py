from typing import Optional, Union

from bcg_edi_835_parser.elements import Element

class Integer(Element):
 
    def parser(self, value: str) -> Optional[Union[int, float]]:
        if value == '':
            return None
        
        try:
            return int(value)
        except:
            pass
            
        return value

