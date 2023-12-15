from src.abstract.abstractas import Abstract
from src.manejadorXml import Estructura


class CallFunction(Abstract):
    def __init__(self, row, column, nombre ,listaParametros):
        self.nombre = nombre
        self.listaParametros = listaParametros
        super().__init__(row, column)
        
    def accept(self, visitor, environment):
        visitor.visit(self, environment)

    def interpretar(self, environment):
        print("Ejecutar Llamada funcion nombre:",self.nombre)

