from src.abstract.abstractas import Abstract
from src.manejadorXml import Estructura

class ProcedureDeclaration(Abstract):
    def __init__(self, fila, columna, nombre, listaParametros,instrucciones):
        self.nombre = nombre
        self.listaParametros = listaParametros
        self.instrucciones = instrucciones
        super().__init__(fila, columna)

    def accept(self, visitor, environment):
        print("aceptando procedure",self.nombre,self.listaParametros)
        visitor.visit(self, environment)
        ##visitor.visitProcedure(self,environment)

    def interpretar(self, environment):
        print("Ejecutar Procedure",self.nombre,self.listaParametros)

