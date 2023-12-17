from src.abstract import Abstract
from src.ast import WhereClause


class ColumnAssignments(Abstract):
    def __init__(self, fila, columna, column_ref, expr):
        super().__init__(fila, columna)
        self.column_ref = column_ref
        self.expr = expr

    def accept(self, visitor, environment):
        self.expr.accept(visitor, environment)
        visitor.visit(self, environment)

    def interpretar(self, environment):
        return super().interpretar(environment)


class Update(Abstract):
    def __init__(self, fila, columna, table, assignments: list, where_clause: WhereClause, db=None):
        super().__init__(fila, columna)
        self.table = table
        self.assignments = assignments
        self.where_clause = where_clause
        self.db = db

    def accept(self, visitor, environment):
        self.where_clause.accept(visitor, environment)
        for assignment in self.assignments:
            assignment.accept(visitor, environment)
        visitor.visit(self, environment)

    def interpretar(self, environment):
        print('ejecutar update')
