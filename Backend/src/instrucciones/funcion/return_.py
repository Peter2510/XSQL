from src.expresiones.variable import Variable
from src.abstract.abstractas import Abstract

class Return_(Abstract):
    def __init__(self, row,column, instruction):
        super().__init__(row,column)
        self.instruction = instruction

    def accept(self, visitor, environment):
        visitor.visit(self,environment)
        
    def interpretar(self,environment):
        val = self.instruction.interpretar(environment)
        var = Variable()
        var.type = val.type
        var.value = val.value
        return var