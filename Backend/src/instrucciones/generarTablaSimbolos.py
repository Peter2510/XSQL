from src.manejadorXml import Estructura
from src.instrucciones.funcion.string_ import String_


class GenerateSymbolTable():
    
    def __init__(self, name, environment):
        self.name = name
        self.environment = environment
        
    def saveST(self):
        for var in self.environment:
            variable = {}
            if isinstance(var.type,String_):
                variable["id"] = var.id
                tm = var.type.size.interpretar(self.environment)
                variable["tipo"] = var.type.type.name + "(" + str(tm.value) + ")"
                variable["valor"] = var.value
            else:
                variable["id"] = var.id
                variable["tipo"] = var.type.name
                variable["valor"] = var.value
        fun = {}
        fun["Entorno"] = self.name
        fun["datos"] = variable
        Estructura.tablasSimbolos.append(fun)
        