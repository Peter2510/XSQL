from src.manejadorXml import Estructura
from src.abstract.abstractas import Abstract


class FunctionDeclaration(Abstract):
    def __init__(self, row, column , id, params, type_, body):
        super().__init__(row,column)
        self.id = id
        self.params = params
        self.type = type_
        self.body = body

    def accept(self, visitor, environment):
        visitor.visit(self, environment)
        
    def interpretar(self, environment):
        
        from src.visitor.tableVisitor import SymbolTableVisitor
        visit = SymbolTableVisitor(environment)
        self.accept(visit, environment)
        if visit.correct:
            return {'tipo': 'funcion', 'resultado': f"Se guardó la función '{self.id}' en la base de datos: {Estructura.nombreActual} "}
        