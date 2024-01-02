from src.instrucciones.generarTablaSimbolos import GenerateSymbolTable
from src.ast.select import Select
from src.manejadorXml import Estructura
from src.instrucciones.funcion.param_function import FunctionParam
from src.abstract.abstractas import Abstract
from src.ejecucion.environment import Environment

class StmWhile(Abstract):
    def __init__(self, row, column,condicion, instrucciones):
        super().__init__(row,column)
        self.condicion = condicion
        self.instrucciones = instrucciones
        

    def accept(self, visitor, environment = None):
        self.condicion.accept(visitor,environment)        
        for instr in self.instrucciones:
            if isinstance(instr,list):
                for i in instr:
                    i.accept(visitor,environment)
            else:
                instr.accept(visitor,environment)
        
            
    def interpretar(self, environment):
        env = Environment(environment)
        print("entro a while")
        print("condicion",self.condicion.interpretar(env).value)
        while self.condicion.interpretar(env).value:
            print("condicion",self.condicion.interpretar(env).value)
            for i in self.instrucciones:
                if isinstance(i,list):
                    for j in i:
                        j.interpretar(env)
                elif isinstance(i,Select):
                    Estructura.selectFunciones.append(i.interpretar(environment))
                else:
                    i.interpretar(env)  
            GST = GenerateSymbolTable("while",env)
            GST.saveST()
        
        