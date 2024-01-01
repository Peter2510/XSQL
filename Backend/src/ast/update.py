from src.abstract import Abstract
from src.ast import WhereClause, TableColumn
from .utils import add_prefix_to_keys, remove_prefix_to_keys, apply_update_expressions
from src.manejadorXml.Estructura import actualizar_datos_en_xml


class ColumnAssignments(Abstract):
    def __init__(self, fila, columna, column_ref: TableColumn, expr):
        super().__init__(fila, columna)
        self.column_ref = column_ref
        self.expr = expr

    def accept(self, visitor, environment):
        self.column_ref.accept(visitor, environment)
        self.expr.accept(visitor, environment)
        visitor.visit(self, environment)

    def interpretar(self, environment):
        return super().interpretar(environment)


class Update(Abstract):
    def __init__(self, fila, columna, table, assignments: list[ColumnAssignments], where_clause: WhereClause):
        super().__init__(fila, columna)
        self.table = table
        self.assignments = assignments
        self.where_clause = where_clause

    def accept(self, visitor, environment):
        self.where_clause.accept(visitor, environment)
        for assignment in self.assignments:
            assignment.accept(visitor, environment)
        visitor.visit(self, environment)

    def interpretar(self, environment):
        from src.visitor.check_expressions_visitor import SqlExpressionsVisitor
        from src.visitor import UpdateVisitor, AssignmentsVisitor
        update_visitor = UpdateVisitor(environment)
        visitor_expressions = SqlExpressionsVisitor(environment)
        assignments_visitor = AssignmentsVisitor(environment)

        self.accept(update_visitor, environment)

        if not update_visitor.correct:
            return None

        self.table_object = update_visitor.table_object

        self.accept(visitor_expressions, environment)

        if not visitor_expressions.correct:
            return None

        self.accept(assignments_visitor, environment)

        if not assignments_visitor.correct:
            return None

        # pp = pprint.PrettyPrinter(indent=2, compact=False, depth=10)

        data = add_prefix_to_keys(self.table_object["data"]["datos"], self.table)

        environment.altered_records = 0
        data_filtered = list(
            map(apply_update_expressions(where_expr=self.where_clause.expr, assign_lst=self.assignments,
                                         environment=environment),
                data))

        environment.record = {}
        altered_records = environment.altered_records
        environment.altered_records = 0

        data_to_write = remove_prefix_to_keys(data_filtered, self.table)
        # pp.pprint(data)
        # print('data filtered:')
        # pp.pprint(data_filtered)

        altered = actualizar_datos_en_xml(self.table, data_to_write)
        if altered is None:
            environment.addError("Semántico", "Update", "Error al actualizar", self.fila, self.columna)
            return None

        return {'tipo': 'update', 'resultado': f"Registros actualizados {altered_records}"}
