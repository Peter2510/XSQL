from abc import ABC, abstractmethod
from ..instruction.functions.simple_function import SimpleFunction

class Visitor(ABC):
      
    @abstractmethod
    def visitSimpleFunction(self, SimpleFunction:SimpleFunction):
        pass
    