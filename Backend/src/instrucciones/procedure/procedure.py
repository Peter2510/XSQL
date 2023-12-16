from src.abstract.abstractas import Abstract
from src.manejadorXml import Estructura

class Procedure(Abstract):
    def __init__(self, fila, columna, nombre, listaParametros,instrucciones):
        self.nombre = nombre
        self.listaParametros = listaParametros
        self.instrucciones = instrucciones
        super().__init__(fila, columna)

    def interpretar(self, tablaSimbolos):
        print("Ejecutar Procedure",self.nombre,self.listaParametros)

