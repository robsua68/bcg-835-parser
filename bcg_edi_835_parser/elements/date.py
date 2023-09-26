from ctypes import Union
from typing import Optional
from datetime import datetime
from warnings import warn

from bcg_edi_835_parser.elements import Element

class Date(Element):
    """Date"""
    
    def parser(self, value: str) -> Union(datetime, str):
        if len(value) == 10:
            year, month, day, minute, second = [int(value[i:i + 2]) for i in range(0, len(value), 2)]
            return datetime(2000 + year, month, day, minute, second)
        
        if len(value) == 8:
            year, month, day = int(value[:4]), int(value[4:6]), int(value[6:])
            return datetime(year, month, day)
        
        else:
            warn(f'Unable to parse date: {value} into a datetime')
            return value
