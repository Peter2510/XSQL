from abc import ABC, abstractmethod

from visitor.visitor import Visitor

class Instruction(ABC):
    
    def __init__(self,line,column):
        super().__init__()
        self.line = line
        self.column = column
       
    @abstractmethod
    def accept(self,visitor:Visitor):
        pass
