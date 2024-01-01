from src.visitor import Visitor
from src.ast import Update, ColumnAssignments
from src.manejadorXml import Estructura
from src.visitor import ValidateColumnVisitor


class AssignmentsVisitor(Visitor):

    def visitColumnAssignments(self, node: ColumnAssignments, environment):
        table_column = node.column_ref
        expr = node.expr
        if table_column.tipo != expr.tipo:
            self.log_error(
                msg=f"No se puede realizar la asignación {table_column.id}({table_column.tipo}) = {node.expr.tipo}",
                column=node.columna, row=node.fila, lexeme="UPDATE")


class UpdateVisitor(Visitor):

    def __init__(self, environment):
        super().__init__(environment)
        self.table_object = None

    def visitUpdate(self, node: Update, environment):
        names = [node.table]
        valid, msg_or_tables = Estructura.comprobar_tablas(tablas=names)
        if not valid:
            self.log_error(msg_or_tables, node.fila, node.columna, "UPDATE")
        else:
            self.table_object = msg_or_tables[0]

        if not self.correct:
            return None

        column_visitor = ValidateColumnVisitor(environment, [self.table_object])
        node.accept(column_visitor, environment)
        self.correct = self.correct and column_visitor.correct
