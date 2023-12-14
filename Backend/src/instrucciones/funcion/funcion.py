from src.abstract.abstractas import Abstract
from src.manejadorXml import Estructura


class Funcion(Abstract):
    def __init__(self, fila, columna, nombre,listaParametros,tipoDato,instrucciones):
        self.nombre = nombre
        self.listaParametros = listaParametros
        self.tipoDato = tipoDato
        self.instrucciones = instrucciones
        super().__init__(fila, columna)

    def accept(self, visitor, environment):
        ##validacioens
        print("Ejecutar validaciones de la funcion")
        pass

    def interpretar(self, tablaSimbolos):
        print("Ejecutar Funcion: nombre:",self.nombre,self.listaParametros,self.tipoDato)

