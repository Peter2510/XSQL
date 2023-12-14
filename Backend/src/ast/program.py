from ..abstract.abstractas import Abstract

class Program(Abstract):
    def __init__(self, fila, columna, statements: list):
        super().__init__(fila, columna)
        self.statements = statements


    def accept(self, visitor, environment):
        for stmt in self.statements:
            stmt.accept(visitor, environment)
        visitor.visit(self, environment)

    def interpretar(self, environment):
        for stmt in self.statements:
            print(stmt.interpretar(environment))


