from src.abstract.abstractas import Abstract
from src.manejadorXml import Estructura

class ProcedureDeclaration(Abstract):
    def __init__(self, fila, columna, id, listaParametros,instrucciones):
        self.id = id
        self.params = listaParametros
        self.body = instrucciones
        super().__init__(fila, columna)

    def accept(self, visitor, environment):
        visitor.visit(self, environment)

    def interpretar(self, environment):
        from src.visitor.tableVisitor import SymbolTableVisitor
        visit = SymbolTableVisitor(environment)
        self.accept(visit, environment)
        if visit.correct:
            return {'tipo': 'procedure', 'resultado': f"Se guardó el procedimiento '{self.id}' en la base de datos: {Estructura.nombreActual} "}

