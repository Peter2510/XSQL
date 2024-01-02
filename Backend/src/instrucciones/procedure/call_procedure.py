from src.abstract.abstractas import Abstract
from src.manejadorXml import Estructura


class CallProcedure(Abstract):
    def __init__(self, fila, columna, nombre ,listaParametros):
        self.id = nombre
        self.parametros = listaParametros
        super().__init__(fila, columna)
        
    def accept(self, visitor, environment):
        visitor.visit(self, environment)

    def interpretar(self, environment):
        from src.visitor.tableVisitor import SymbolTableVisitor
        visit = SymbolTableVisitor(environment)
        self.accept(visit, environment)

