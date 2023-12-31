from src.ast.select import Select
from src.manejadorXml import Estructura
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
        if self.list_elseif != None:
            for elseif in self.list_elseif:
                elseif.accept(visitor,environment)
        if self.else_ != None:
            self.else_.accept(visitor,environment)
 
            
    def interpretar(self, environment):
        print("SON IF",self._if,self.list_elseif,self.else_)
        env = Environment(environment)
        if self._if.condition.interpretar(environment).value:
            print("entro a if")
            for i in self._if.instructions:
                if isinstance(i,list):
                    for j in i:
                        j.interpretar(env)
                elif isinstance(i,Select):
                    Estructura.selectFunciones.append(i.interpretar(environment))
                else:
                    i.interpretar(env)
        elif self.list_elseif != None:
            elseValido = False
            for elseif in self.list_elseif:
                print("entro a else if")
                if elseif.condition.interpretar(environment).value:
                    
                    for i in elseif.instructions:
                        if isinstance(i,list):
                            for j in i:
                                j.interpretar(env)
                        elif isinstance(i,Select):
                            Estructura.selectFunciones.append(i.interpretar(environment))
                        else:
                            i.interpretar(env)
                    elseValido = True
                    break
            if not elseValido:
                if self.else_ != None:
                    print("entro a else ")
                    for i in self.else_.instructions:
                        if isinstance(i,list):
                            for j in i:
                                j.interpretar(env)
                        elif isinstance(i,Select):
                            Estructura.selectFunciones.append(i.interpretar(environment))
                        else:
                            i.interpretar(env)
                
        else:
            if self.else_ != None:
                print("entro a else ")
                for i in self.else_.instructions:
                    if isinstance(i,list):
                        for j in i:
                            j.interpretar(env)
                    elif isinstance(i,Select):
                        Estructura.selectFunciones.append(i.interpretar(environment))
                    else:
                        i.interpretar(env)
