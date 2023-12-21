from ..abstract import Abstract


class Table(Abstract):
    def __init__(self, fila, columna, id):
        super().__init__(fila, columna)
        self.id = id

    def accept(self, visitor, environment):
        visitor.visit(self, environment)

    def interpretar(self, environment):
        return self.id


# TODO: Validar que las tablas existan en nombreActual


class TableColumn(Abstract):
    def __init__(self, fila, columna, id, table=None, tipo=None):
        super().__init__(fila, columna)
        self.table = table
        self.id = id
        self.tipo = tipo

    def accept(self, visitor, environment):
        visitor.visit(self, environment)

    def interpretar(self, environment):


        return self.id


class FromClause(Abstract):
    def __init__(self, fila, columna, tables: list[Table]):
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


# TODO: Validar que en las expresiones los ids sean columnas validas según las tablas del From


class Select(Abstract):
    def __init__(self, fila, columna, columns: list, from_clause: FromClause | None = None,
                 where_clause: WhereClause | None = None, tables=None):
        super().__init__(fila, columna)
        if tables is None:
            tables = []
        self.columns = columns
        self.from_clause = from_clause
        self.where_clause = where_clause
        self.tables = tables

    def accept(self, visitor, environment):
        if self.from_clause is not None:
            self.from_clause.accept(visitor, environment)
        if self.where_clause is not None:
            self.where_clause.accept(visitor, environment)
        for col in self.columns:
            col.accept(visitor, environment)
        visitor.visit(self, environment)

    def interpretar(self, environment):
        from src.visitor import TablesValidVisitor
        visitor = TablesValidVisitor(environment)
        visitor.visit(self, environment)
        if visitor.correct:
            pass
        else:
            return None


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
        self.expr.accept(visitor, environment)
        visitor.visit(self, environment)

    def interpretar(self, environment):
        return 'interpretar alias'
