from src.abstract.abstractas import Abstract
from src.manejadorXml import Estructura

class AlterProcedure(Abstract):
    def __init__(self, fila, columna, nombre, listaParametros,instrucciones):
        self.id = nombre
        self.params = listaParametros
        self.body = instrucciones
        super().__init__(fila, columna)

    def accept(self, visitor, environment):
        visitor.visit(self, environment)

    def interpretar(self, environment):
        from src.visitor.tableVisitor import SymbolTableVisitor
        visit = SymbolTableVisitor(environment)
        if visit.correct == True:
            self.accept(visit, environment)
        if visit.correct:
            return {'tipo': 'funcion', 'resultado': f"Se actualizó correctamente el procedimiento '{self.id}' de la base de datos: {Estructura.nombreActual} "}

