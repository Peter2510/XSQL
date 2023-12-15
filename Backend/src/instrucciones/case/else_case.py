from src.instrucciones.funcion.param_function import FunctionParam
from src.abstract.abstractas import Abstract
from src.ejecucion.environment import Environment

class ElseCase(Abstract):
    def __init__(self, row, column ,instruction):
        super().__init__(row,column)
        self.instructions = instruction

    def accept(self, visitor, environment = None):
        
        visitor.visit(self,environment)
            
    def interpretar(self, environment):
        print("interpretando else case")
