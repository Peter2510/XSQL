from abc import ABC
from ..expresiones import aritmeticas, logicos, primitivos, relacional
from src.ast import (
    Select, FromClause, Table,
    WhereClause, AllColumns, TableColumn,
    AliasSelect, SelectAssign, Program,
    ColumnAssignments, Update, Delete
)


class Visitor(ABC):
    def __init__(self, environment):
        self.environment = environment
        self.correct = True

    def log_error(self, msg, row=None, column=None):
        self.correct = False
        print(msg, f"ln: {row}, col: {column}")

    def visit(self, node, environment):
        if not self.correct:
            return

        if isinstance(node, aritmeticas.Aritmeticas):
            self.visitAritmeticas(node, environment)
        elif isinstance(node, logicos.Logico):
            self.visitLogico(node, environment)
        elif isinstance(node, primitivos.Primitivo):
            self.visitPrimitivo(node, environment)
        elif isinstance(node, relacional.Relacional):
            self.visitRelacional(node, environment)
        elif isinstance(node, Select):
            self.visitSelect(node, environment)
        elif isinstance(node, FromClause):
            self.visitFromClause(node, environment)
        elif isinstance(node, Table):
            self.visitTable(node, environment)
        elif isinstance(node, WhereClause):
            self.visitWhereClause(node, environment)
        elif isinstance(node, AllColumns):
            self.visitAllColumns(node, environment)
        elif isinstance(node, TableColumn):
            self.visitTableColumn(node, environment)
        elif isinstance(node, AliasSelect):
            self.visitAliasSelect(node, environment)
        elif isinstance(node, SelectAssign):
            self.visitSelectAssign(node, environment)
        elif isinstance(node, Program):
            self.visitProgram(node, environment)
        elif isinstance(node, ColumnAssignments):
            self.visitColumnAssignments(node, environment)
        elif isinstance(node, Update):
            self.visitUpdate(node, environment)
        elif isinstance(node, Delete):
            self.visitDelete(node, environment)

    def visitAritmeticas(self, node, environment):
        pass

    def visitLogico(self, node, environment):
        pass

    def visitPrimitivo(self, node, environment):
        pass

    def visitRelacional(self, node, environment):
        pass

    def visitSelect(self, node, environment):
        pass

    def visitFromClause(self, node, environment):
        pass

    def visitTable(self, node, environment):
        pass

    def visitWhereClause(self, node, environment):
        pass

    def visitAllColumns(self, node, environment):
        pass

    def visitTableColumn(self, node, environment):
        pass

    def visitAliasSelect(self, node, environment):
        pass

    def visitSelectAssign(self, node, environment):
        pass

    def visitProgram(self, node, environment):
        pass

    def visitColumnAssignments(self, node, environment):
        pass

    def visitUpdate(self, node, environment):
        pass

    def visitDelete(self, node, environment):
        pass
