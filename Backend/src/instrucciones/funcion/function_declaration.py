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
        pass
        
    def interpretar(self, environment):
        from src.visitor.tableVisitor import SymbolTableVisitor
        visit = SymbolTableVisitor(environment)
        if visit.correct == True:
            self.accept(visit, environment)
        
              
