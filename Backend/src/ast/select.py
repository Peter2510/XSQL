from ..abstract import Abstract


class Select(Abstract):
    def __init__(self, fila, columna, columns: list, from_clause=None, where_clause=None, db=None):
        super().__init__(fila, columna)
        self.columns = columns
        self.from_clause = from_clause
        self.where_clause = where_clause
        self.db = db

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


class Table(Abstract):
    def __init__(self, fila, columna, id):
        super().__init__(fila, columna)
        self.id = id

    def accept(self, visitor, environment):
        visitor.visit(self, environment)

    def interpretar(self, environment):
        return self.id


class TableColumn(Abstract):
    def __init__(self, fila, columna, id, table=None):
        super().__init__(fila, columna)
        self.table = table
        self.id = id

    def accept(self, visitor, environment):
        visitor.visit(self, environment)

    def interpretar(self, environment):
        return self.id


class FromClause(Abstract):
    def __init__(self, fila, columna, tables: list):
        super().__init__(fila, columna)
        self.tables = tables

    def accept(self, visitor, environment):
        for table in self.tables:
            table.accept(visitor, environment)
        visitor.visit(self, environment)

    def interpretar(self, environment):
        for table in self.tables:
            print(table.interpretar(environment))


class WhereClause(Abstract):
    def __init__(self, fila, columna, expr):
        super().__init__(fila, columna)
        self.expr = expr

    def accept(self, visitor, environment):
        self.expr.accept(visitor, environment)
        visitor.visit(self, environment)

    def interpretar(self, environment):
        print(self.expr.interpretar)


class AllColumns(Abstract):
    def __init__(self, fila, columna):
        super().__init__(fila, columna)

    def accept(self, visitor, environment):
        visitor.visit(self, environment)

    def interpretar(self, environment):
        return '*'


class SelectAssign(Abstract):
    def __init__(self, fila, columna, variable, function):
        super().__init__(fila, columna)
        self.variable = variable
        self.function = function

    def accept(self, visitor, environment):
        self.function.accept(self, environment)
        visitor.visit(self, environment)

    def interpretar(self, environment):
        return 'id_declare = function'


class AliasSelect(Abstract):
    def __init__(self, fila, columna, id, expr):
        super().__init__(fila, columna)
        self.id = id
        self.expr = expr

    def accept(self, visitor, environment):
        self.expr.accept(self, environment)
        visitor.visit(self, environment)

    def interpretar(self, environment):
        return 'interpretar alias'
