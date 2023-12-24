from src.instrucciones.funcion.param_function import FunctionParam
from src.abstract.abstractas import Abstract
from src.ejecucion.environment import Environment

class StmIf(Abstract):
    def __init__(self, row, column,_if,list_elseif,else_):
        super().__init__(row,column)
        self._if = _if
        self.list_elseif = list_elseif
        self.else_ = else_

    def accept(self, visitor, environment = None):
        self._if.accept(visitor,environment)
        # if self.list_elseif != None:
            # for elseif in self.list_elseif:
                # elseif.accept(visitor,environment)
        if self.else_ != None:
            self.else_.accept(visitor,environment)
 
            
    def interpretar(self, environment):
        print("interpretando if general")
