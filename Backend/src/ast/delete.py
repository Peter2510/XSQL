import pprint
from src.abstract import Abstract
from src.ast import WhereClause
from .utils import filter_where_delete, add_prefix_to_keys, remove_prefix_to_keys
from src.manejadorXml.Estructura import actualizar_datos_en_xml


class Delete(Abstract):
    def __init__(self, fila, columna, table, where_clause: WhereClause):
        super().__init__(fila, columna)
        self.table = table
        self.where_clause = where_clause
        self.table_object = None

    def accept(self, visitor, environment):
        self.where_clause.accept(visitor, environment)
        visitor.visit(self, environment)

    def interpretar(self, environment):
        from src.visitor.check_expressions_visitor import SqlExpressionsVisitor
        from src.visitor import DeleteVisitor
        visitor_delete = DeleteVisitor(environment)
        visitor_expressions = SqlExpressionsVisitor(environment)

        self.accept(visitor_delete, environment)

        if not visitor_delete.correct:
            return None

        self.table_object = visitor_delete.table_object

        self.accept(visitor_expressions, environment)

        if not visitor_expressions.correct:
            return None

        # pp = pprint.PrettyPrinter(indent=2, compact=False, depth=10)

        data = add_prefix_to_keys(self.table_object["data"]["datos"], self.table)

        data_filtered = list(filter(filter_where_delete(self.where_clause.expr, environment),
                                    data))

        data_to_write = remove_prefix_to_keys(data_filtered, self.table)
        # pp.pprint(data)
        # print('data filtered:')
        # pp.pprint(data_filtered)

        altered = actualizar_datos_en_xml(self.table, data_to_write)
        if altered is None:
            environment.addError("Semántico", "Delete", "Error al eliminar", self.fila, self.columna)
            return None

        return {'tipo': 'delete', 'resultado': f"Registros alterados {len(data) - len(data_filtered)}"}
