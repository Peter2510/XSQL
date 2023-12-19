from src.visitor import Visitor
from src.ast import Select, Table, FromClause, TableColumn
from src.manejadorXml import Estructura


class ValidateColumnVisitor(Visitor):

    def visitTableColumn(self, node: TableColumn, environment):
        tables = environment.tables
        if tables is None:
            self.log_error(msg="No se seleccionó una tabla", column=node.columna, row=node.fila)
            return

        if node.table is not None and node.table not in tables:
            self.log_error(msg=f"Columna {node.table}.{node.id} no encontrada", column=node.columna, row=node.fila)
            return

        check_tables = [node.table] if node.table is not None else tables
        tables_found = Estructura.find_tables(tables=check_tables, name=node.id)
        if len(tables_found) == 0:
            return False, f"{node.id} no existe"

        if len(tables_found) > 1:
            return False, f"La columna {node.id} es ambigüa"

        db_table = tables_found[0]
        tipo = db_table.get("tipo", "")


class TablesValidVisitor(Visitor):

    def __init__(self, environment):
        super().__init__(environment)

    def visitFromClause(self, node: FromClause, environment):
        tables = node.tables
        names = [table.id for table in tables]
        valid, msg = Estructura.comprobar_tablas(tablas=names)
        if not valid:
            self.log_error(msg, node.fila, node.columna)

    def visitSelect(self, node: Select, environment):
        if node.from_clause is not None:
            names = [table.id for table in node.from_clause.tables]
            node.tables = names

        # Agregar las tablas validadas al environment
        environment.tables = node.tables
        column_visitor = ValidateColumnVisitor(environment)
        node.accept(column_visitor, environment)
        # Limpiar environment después de validar
        environment.tables = None
