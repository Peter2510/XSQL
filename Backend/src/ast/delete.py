from src.abstract import Abstract
from src.ast import WhereClause


class Delete(Abstract):
    def __init__(self, fila, columna, table, where_clause: WhereClause, db=None):
        super().__init__(fila, columna)
        self.table = table
        self.where_clause = where_clause
        self.db = db

    def accept(self, visitor, environment):
        self.where_clause.accept(visitor, environment)
        visitor.visit(self, environment)

    def interpretar(self, environment):
        print('interpretar delete')
