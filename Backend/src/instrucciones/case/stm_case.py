from src.ast.delete import Delete
from src.ast.update import Update
from src.instrucciones.generarTablaSimbolos import GenerateSymbolTable
from src.ast.select import Select
from src.manejadorXml import Estructura
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
        whenValido = False
        env = Environment(environment)
        for when in self.list_when:
            if when.condition.interpretar(environment).value:
                
                for i in when.instructions:
                    if isinstance(i,list):
                        for j in i:
                            j.interpretar(env)
                    elif isinstance(i,Select):
                        Estructura.selectFunciones.append(i.interpretar(environment))                            
                    elif isinstance(i,Update):
                        Estructura.selectFunciones.append(i.interpretar(environment))                            
                    elif isinstance(i,Delete):
                        Estructura.selectFunciones.append(i.interpretar(environment))                            
                    else:
                        i.interpretar(env)
                whenValido = True
                #GST = GenerateSymbolTable("when",env)
                #GST.saveST()
                break
        if not whenValido:
            if self.else_case != None:
                
                for i in self.else_case.instructions:
                    if isinstance(i,list):
                        for j in i:
                            j.interpretar(env)
                    elif isinstance(i,Select):
                        Estructura.selectFunciones.append(i.interpretar(environment))
                    elif isinstance(i,Update):
                        Estructura.selectFunciones.append(i.interpretar(environment))
                    elif isinstance(i,Delete):
                        Estructura.selectFunciones.append(i.interpretar(environment))
                    else:
                        i.interpretar(env)
                #GST = GenerateSymbolTable("when",env)
                #GST.saveST()
            
