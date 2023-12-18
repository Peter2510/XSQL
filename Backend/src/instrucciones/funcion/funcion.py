from src.abstract.abstractas import Abstract
from src.manejadorXml import Estructura


class Funcion():
    def __init__(self,nombre,tablaSimbolos):
        self.nombre = nombre
        self.tablaSimbolos = tablaSimbolos
        self.instrucciones = []
        
    def interpretar(self, environment):
        print("Ejecutar de cada instruccion",self.nombre)
        

class TablaSimbolos():
    
    def __init__(self,nombre,padre=None):
        self.nombre = nombre
        self.padre = padre
        self.variables = {}
        
    def existeVariable(self,nombreVariable):
        if nombreVariable in self.variables:
            return True
        return False
    
    def agregarVariable(self,nombreVariable,data):
        self.variables[nombreVariable] = data
        
    def obtenerVariable(self,nombreVariable):
        return self.variables[nombreVariable]
        
class Simbolo():
    
    def __init__(self,tipo,valor):
        self.tipo = tipo
        self.valor = valor
        
        

