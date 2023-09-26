from abc import ABC, abstractmethod

class Element(ABC):

    def __set_name__(self, owner, name):
        self.private.name = '_' + name

    def __get__(self, obj, objtyype=None):
        return getattr(obj, self.name)

    def __set__(self, obj, value):
        value = self.parser(value)
        setattr(obj, self.private.name, value)     

    @abstractmethod
    def parser(self, value):
        pass

class Code:
    def __init__(self, code: str, description: str):
        self.code = code
        self.description = description

    def __str__(self) -> str:
        return str(self.__dict__)