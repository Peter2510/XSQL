from src.visitor import Visitor
from src.ast import Delete, WhereClause
from src.manejadorXml import Estructura
from src.ejecucion.type import Type
from src.visitor import ValidateColumnVisitor


class DeleteVisitor(Visitor):

    def __init__(self, environment):
        super().__init__(environment)
        self.table_object = None

    def visitDelete(self, node: Delete, environment):
        names = [node.table]
        valid, msg_or_tables = Estructura.comprobar_tablas(tablas=names)
        if not valid:
            self.log_error(msg_or_tables, node.fila, node.columna, "DELETE")
        else:
            self.table_object = msg_or_tables[0]

        if not self.correct:
            return None

        column_visitor = ValidateColumnVisitor(environment, [self.table_object])
        node.accept(column_visitor, environment)
        self.correct = self.correct and column_visitor.correct
