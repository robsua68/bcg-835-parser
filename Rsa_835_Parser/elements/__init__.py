""" Elements module """
from abc import ABC, abstractmethod

class Element(ABC):
    """Element Class"""

    def __init__(self):
        self.private = type("", (), {})()
        self.private_name = None

    def __set_name__(self, owner, name):
        self.private_name = "_" + name

    def __get__(self, obj, objtyype=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        value = self.parser(value)
        setattr(obj, self.private_name, value)

    @abstractmethod
    def parser(self, value):
        """Parser method"""


class Code:
    """Code Class"""

    def __init__(self, code: str, description: str):
        self.code = code
        self.description = description

    def __str__(self) -> str:
        return str(self.__dict__)
