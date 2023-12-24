import pprint
from ..abstract import Abstract
from .utils import add_prefix_to_keys, filter_where_clause, apply_column_expressions, cartesian_product
from src.ejecucion.type import Type


class Table(Abstract):
    def __init__(self, fila, columna, id):
        super().__init__(fila, columna)
        self.id = id

    def accept(self, visitor, environment):
        visitor.visit(self, environment)

    def interpretar(self, environment):
        return self.id


class TableColumn(Abstract):
    def __init__(self, fila, columna, id, table=None, tipo=None):
        super().__init__(fila, columna)
        self.table = table
        self.id = id
        self.tipo = tipo

    def __str__(self):
        return f"{self.table}.{self.id}"

    def accept(self, visitor, environment):
        visitor.visit(self, environment)

    def interpretar(self, environment):
        record = environment.record
        value = record.get(f"{self.table}.{self.id}", 0)
        if self.tipo == Type.INT:
            return int(value)
        elif self.tipo == Type.BIT:
            return bool(int(value))
        elif self.tipo == Type.DECIMAL:
            return float(value)

        return value


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
        self.data = []

    def get_data_joined(self):
        # TODO: Implement
        tables = []
        for record in self.data:
            name = record["name"]
            data = record["data"]["datos"]
            tables.append(add_prefix_to_keys(data, name))

        return cartesian_product(*tables)

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
        from src.visitor.check_expressions_visitor import SqlExpressionsVisitor
        visitor = TablesValidVisitor(environment)
        visitor_expressions = SqlExpressionsVisitor(environment)
        self.accept(visitor, environment)

        if not visitor.correct:
            return None

        self.data = visitor.tables

        self.accept(visitor_expressions, environment)

        if not visitor_expressions.correct:
            return None

        if self.from_clause is None and self.where_clause is None:
            result = ''
            for column in self.columns:
                print('expr: ', str(column))
                result += f"{column.interpretar(environment)}\n"

            print('result: ', result)
            return result

        data = self.get_data_joined()
        # Apply where expr
        data_filtered = list(filter(filter_where_clause(self.where_clause.expr, environment),
                                    data)) if self.where_clause is not None else data

        # Apply expressions in columns
        environment.record = {}
        final_data = list(map(apply_column_expressions(self.columns, environment), data_filtered))
        pp = pprint.PrettyPrinter(indent=2, compact=False, depth=10)
        pp.pprint(final_data)

        return final_data


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
        self.valor = None

    def __str__(self):
        return self.id

    def accept(self, visitor, environment):
        self.expr.accept(visitor, environment)
        visitor.visit(self, environment)

    def interpretar(self, environment):
        self.valor = self.expr.interpretar(environment)
        return self.valor
