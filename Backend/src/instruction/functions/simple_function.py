from visitor.visitor import Visitor
from ..instruction import Instruction

class SimpleFunction(Instruction):
    
    def __init__(self, id, instructions, line, column):
        super().__init__(line,column)  
        self.id = id
        self.instructions = instructions
        
    def accept(self, visitor:Visitor):
        return visitor.visitSimpleFunction(self)