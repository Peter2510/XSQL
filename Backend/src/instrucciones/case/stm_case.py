from src.instrucciones.funcion.param_function import FunctionParam
from src.abstract.abstractas import Abstract
from src.ejecucion.environment import Environment

class StmCase(Abstract):
    def __init__(self, row, column,list_when,else_case,alias):
        super().__init__(row,column)
        self.list_when = list_when
        self.else_case = else_case
        self.alias = alias

    def accept(self, visitor, environment = None):       
        for when in self.list_when:
            when.accept(visitor,environment)
        if self.else_case != None:
            self.else_case.accept(visitor,environment)
        
        visitor.visit(self,environment)
            
    def interpretar(self, environment):
        print("interpretando case general")
