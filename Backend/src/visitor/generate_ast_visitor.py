import gvgen
from .visitor import Visitor
from src.instrucciones.crearTabla import crearTabla
from src.instrucciones.createdb import createDB
from src.instrucciones.funcion.function_declaration import FunctionDeclaration
from src.instrucciones.funcion.alter_function import AlterFunction
from src.instrucciones.procedure.create_procedure import ProcedureDeclaration
from src.instrucciones.procedure.call_procedure import CallProcedure
from src.instrucciones.procedure.alter_procedure import AlterProcedure
from src.instrucciones.truncate.truncateDB import truncateDB
from src.instrucciones.truncate.truncateTabla import truncateTabla
from src.instrucciones.drop.dropDB import dropDB
from src.instrucciones.drop.dropTabla import dropTable
from src.instrucciones.Alter.alterTable import alterTable
from src.instrucciones.usarDB import usarDB
from src.ast import (Select, Delete, FromClause, WhereClause, SQLUnaryExpression, SQLBinaryExpression,
                     SQLLogicalExpression, AliasSelect, TableColumn)
from src.funciones import (Cas, Concatenar, Contar, Hoy, Substraer, Suma)
from src.instrucciones.insert.insert import insertInstruccion
from src.instrucciones.update.update import updateInstruccion


class GenerateASTVisitor(Visitor):
    def __init__(self, environment):
        super().__init__(environment)
        self.graph = gvgen.GvGen()
        self.root = self.graph.newItem("XSQL")

    def get_graph(self):
        return self.graph

    def visitFromClause(self, node: FromClause, environment):
        from_clause_node = self.graph.newItem("FROM")
        for table in node.tables:
            table_node = self.graph.newItem(table.id)
            self.graph.newLink(from_clause_node, table_node)

        node.nd = from_clause_node

    def visitWhereClause(self, node: WhereClause, environment):
        where_clause_node = self.graph.newItem("WHERE")
        self.graph.newLink(where_clause_node, node.expr.nd)
        node.nd = where_clause_node

    def visitAllColumns(self, node, environment):
        node.nd = self.graph.newItem("*")

    def visitAliasSelect(self, node: AliasSelect, environment):
        node.nd = self.graph.newItem(node.id)
        self.graph.newLink(node.nd, node.expr.nd)

    def visitTableColumn(self, node: TableColumn, environment):
        node.nd = self.graph.newItem(f"{node.table}.{node.id}")

    def visitSQLBinaryExpression(self, node: SQLBinaryExpression, environment):
        node.nd = self.graph.newItem(node.operator)
        self.graph.newLink(node.nd, node.left.nd)
        self.graph.newLink(node.nd, node.right.nd)

    def visitSQLLogicalExpression(self, node, environment):
        self.visitSQLBinaryExpression(node, environment)

    def visitSQLUnaryExpression(self, node: SQLUnaryExpression, environment):
        if not isinstance(node.argument, (int, str, float, bool)):
            node.nd = node.argument.nd if (
                    node.argument is not None and node.argument.nd is not None) else self.graph.newItem(
                "Call")
        else:
            node.nd = self.graph.newItem(f"{node.argument}")

    def visitCas(self, node: Cas, environment):
        node.nd = self.graph.newItem("CAS")
        self.graph.newLink(node.nd, node.expr.nd)

    def visitConcatenar(self, node: Concatenar, environment):
        node.nd = self.graph.newItem("CONCATENA")
        for expr in node.expr_lst:
            self.graph.newLink(node.nd, expr.nd)

    def visitContar(self, node: Contar, environment):
        node.nd = self.graph.newItem("CONTAR")

    def visitHoy(self, node: Hoy, environment):
        node.nd = self.graph.newItem("HOY")

    def visitSubstraer(self, node: Substraer, environment):
        node.nd = self.graph.newItem("SUBSTRAER")
        self.graph.newLink(node.nd, node.value.nd)

    def visitSuma(self, node: Suma, environment):
        node.nd = self.graph.newItem("SUMA")
        if not isinstance(node.value, int):
            self.graph.newLink(node.nd, node.value.nd)
        else:
            node_suma = self.graph.newItem(node.value)
            self.graph.newLink(node.nd, node_suma)

    def visitSelect(self, node: Select, environment):
        select_node = self.graph.newItem("SELECT")
        self.graph.newLink(self.root, select_node)
        columns_node = self.graph.newItem("COLUMNS")
        self.graph.newLink(select_node, columns_node)
        for column in node.columns:
            self.graph.newLink(columns_node, column.nd)

        if node.from_clause is not None:
            self.graph.newLink(select_node, node.from_clause.nd)

        if node.where_clause is not None:
            self.graph.newLink(select_node, node.where_clause.nd)

        node.nd = select_node

    def visitDelete(self, node: Delete, environment):
        node.nd = self.graph.newItem("DELETE")
        self.graph.newLink(self.root, node.nd)
        from_node = self.graph.newItem("FROM")
        node_id = self.graph.newItem(node.table)
        self.graph.newLink(from_node, node_id)
        self.graph.newLink(node.nd, from_node)
        self.graph.newLink(node.nd, node.where_clause.nd)
