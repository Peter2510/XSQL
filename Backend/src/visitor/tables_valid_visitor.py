from src.visitor import Visitor
from src.ast import Select, Table, FromClause, TableColumn
from src.manejadorXml import Estructura
from src.ejecucion.type import Type


class ValidateColumnVisitor(Visitor):

    def __init__(self, environment, tables):
        super().__init__(environment)
        self.tables = tables

    def visitTableColumn(self, node: TableColumn, environment):
        if self.tables is None:
            self.log_error(msg="No se seleccionó una tabla", column=node.columna, row=node.fila, lexeme="DB")
            return

        # check_tables = [node.table] if node.table is not None else tables
        tables_found = Estructura.find_tables(tables=self.tables, name=node.id, table_name=node.table)
        if len(tables_found) == 0:
            table_log = f"{node.table}." if node.table is not None else ""
            self.log_error(msg=f"La columna {table_log}{node.id} no existe", column=node.columna, row=node.fila,
                           lexeme="Columna")
            return

        if len(tables_found) > 1:
            self.log_error(msg=f"La columna {node.id} es ambigüa", column=node.columna, row=node.fila, lexeme="Columna")

        db_table = tables_found[0]
        data_tb = db_table.get("data", {})
        name_tb = db_table.get("name", "")
        estructura_tb = data_tb.get("estructura", {})
        column_tb = estructura_tb.get(node.id, {})
        attribute_1 = column_tb.get("Atributo1", {})
        tipo = attribute_1.get("tipo", None)
        column_type = None
        if tipo in 'nvarchar':
            column_type = Type.TEXT
        elif tipo in 'nchar':
            column_type = Type.TEXT
        elif tipo in 'int':
            column_type = Type.INT
        elif tipo in 'bit':
            column_type = Type.BIT
        elif tipo in 'decimal':
            column_type = Type.DECIMAL
        elif tipo in 'date':
            column_type = Type.DATE
        elif tipo in 'datetime':
            column_type = Type.DATETIME
        node.tipo = column_type
        node.table = name_tb


class TablesValidVisitor(Visitor):

    def __init__(self, environment):
        super().__init__(environment)
        self.tables = []

    def visitFromClause(self, node: FromClause, environment):
        tables = node.tables
        names = [table.id for table in tables]
        valid, msg_or_tables = Estructura.comprobar_tablas(tablas=names)
        if not valid:
            self.log_error(msg_or_tables, node.fila, node.columna, "columna")
        else:
            self.tables = msg_or_tables

    def visitSelect(self, node: Select, environment):
        if node.from_clause is not None:
            names = [table.id for table in node.from_clause.tables]
            node.tables = names

        column_visitor = ValidateColumnVisitor(environment, self.tables)
        node.accept(column_visitor, environment)
        self.correct = self.correct and column_visitor.correct
