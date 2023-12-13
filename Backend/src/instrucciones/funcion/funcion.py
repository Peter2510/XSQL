from src.abstract.abstractas import Abstract
from src.manejadorXml import Estructura
from src.ejecucion.datatype import tipoDato

class Funcion(Abstract):
    def __init__(self, fila, columna, nombre,listaParametros,tipoDato:tipoDato,instrucciones):
        self.nombre = nombre
        self.listaParametros = listaParametros
        self.tipoDato = tipoDato
        self.instrucciones = instrucciones
        super().__init__(fila, columna)

    def interpretar(self, tablaSimbolos):
        print("Ejecutar Funcion: nombre:",self.nombre,self.listaParametros,self.tipoDato)

