from src.instrucciones.funcion.param_function import FunctionParam
from src.abstract.abstractas import Abstract
from src.ejecucion.environment import Environment

class ConcatenaSSL(Abstract):
    def __init__(self, row, column):
        super().__init__(row,column)
        

    def accept(self, visitor, environment = None):
        visitor.visit(self, environment)
        
            
    def interpretar(self, environment):
        pass
        
        