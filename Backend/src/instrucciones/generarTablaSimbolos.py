from src.manejadorXml import Estructura
from src.instrucciones.funcion.string_ import String_

class GenerateSymbolTable():
    
    def __init__(self, name, environment):
        self.name = name
        self.environment = environment
        
    def saveST(self):
        fun = {}
        fun["Entorno"] = self.name
        datos = []  # Lista para almacenar las variables
        for var in self.environment:
            variable = {}
            if isinstance(var.type, String_):
                variable["id"] = var.id
                tm = var.type.size.interpretar(self.environment)
                variable["tipo"] = var.type.type.name + "(" + str(tm.value) + ")"
                variable["valor"] = var.value
            else:
                variable["id"] = var.id
                variable["tipo"] = var.type.name
                variable["valor"] = var.value
            datos.append(variable)  # Agregar la variable a la lista
        fun["datos"] = datos  # Asignar la lista de variables a "datos"
        Estructura.tablasSimbolos.append(fun)
