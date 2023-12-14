from src.abstract.abstractas import Abstract
from src.manejadorXml import Estructura


class CallProcedure(Abstract):
    def __init__(self, fila, columna, nombre ,listaParametros):
        self.nombre = nombre
        self.listaParametros = listaParametros
        super().__init__(fila, columna)

    def interpretar(self, environment):
        print("Ejecutar Llamada PROCECURE nombre:",self.nombre)

