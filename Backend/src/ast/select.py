from ..abstract import Abstract

class Select(Abstract):
    def __init__(self, fila, columna, columns: list, from_clause = None, where_clause = None):
        super().__init__(fila, columna)
        self.columns = columns
        self.from_clause = from_clause
        self.where_clause = where_clause


    def accept(self, visitor, environment):
        if self.from_clause is not None:
            self.from_clause.accept(visitor, environment)
        if self.where_clause is not None:
            self.where_clause.accept(visitor, environment)
        for col in self.columns:
            col.accept(visitor, environment)
        visitor.visit(self, environment)

    def interpretar(self, environment):
        for col in self.columns:
            print(col.interpretar(environment))


