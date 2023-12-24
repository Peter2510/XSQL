from src.instrucciones.funcion.param_function import FunctionParam
from src.abstract.abstractas import Abstract
from src.ejecucion.environment import Environment

class AlterFunction(Abstract):
    def __init__(self, row, column , id, params, type_, body):
        super().__init__(row,column)
        self.id = id
        self.params = params
        self.type = type_
        self.body = body

    def accept(self, visitor, environment = None):
        visitor.visit(self,environment)
            
    def interpretar(self, environment):
        from src.visitor.tableVisitor import SymbolTableVisitor
        visit = SymbolTableVisitor(environment)
        if visit.correct == True:
            self.accept(visit, environment)

