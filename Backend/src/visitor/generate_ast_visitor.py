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
from src.ast import Select, Delete
from src.instrucciones.insert.insert import insertInstruccion
from src.instrucciones.update.update import updateInstruccion


class GenerateASTVisitor(Visitor):
    def __init__(self, environment):
        super().__init__(environment)
        self.graph = gvgen.GvGen()
        self.root = self.graph.newItem("XSQL")

    def get_graph(self):
        return self.graph

    def visitSelect(self, node: Select, environment):
        select_node = self.graph.newItem("SELECT")
        self.graph.newLink(self.root, select_node)
        columns_node = self.graph.newItem("COLUMNS")
        self.graph.newLink(select_node, columns_node)
        for _column in node.columns:
            column_node = self.graph.newItem("expr")
            self.graph.newLink(columns_node, column_node)

        if node.from_clause is not None:
            from_clause_node = self.graph.newItem("FROM")
            self.graph.newLink(select_node, from_clause_node)
            for table in node.from_clause.tables:
                table_node = self.graph.newItem(table.id)
                self.graph.newLink(from_clause_node, table_node)

        if node.where_clause is not None:
            where_clause_node = self.graph.newItem("WHERE")
            self.graph.newLink(select_node, where_clause_node)
            expr_node = self.graph.newItem("expr")
            self.graph.newLink(where_clause_node, expr_node)
