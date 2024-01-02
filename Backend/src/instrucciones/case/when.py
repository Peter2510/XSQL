from src.instrucciones.funcion.param_function import FunctionParam
from src.abstract.abstractas import Abstract
from src.ejecucion.environment import Environment

class When(Abstract):
    def __init__(self, row, column , condition,instruction):
        super().__init__(row,column)
        self.condition = condition
        self.instructions = instruction

    def accept(self, visitor, environment = None):
        visitor.visit(self,environment)
            
    def interpretar(self, environment):
        for i in self.instructions:
            if isinstance(i,list):
                for j in i:
                    j.interpretar(environment)
            else:
                i.interpretar(environment)
