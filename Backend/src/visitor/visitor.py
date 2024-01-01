from abc import ABC
from src.expresiones.primitivos import Primitivo
from src.instrucciones.funcion.call_function import CallFunction
from src.instrucciones.funcion.alter_function import AlterFunction
from src.instrucciones.funcion.return_ import Return_
from src.instrucciones.case.else_case import ElseCase
from src.instrucciones.case.when import When
from src.instrucciones.case.stm_case import StmCase
from src.instrucciones.conditionals.else_if_ import ElseIf_
from src.instrucciones.conditionals.else_ import Else_
from src.instrucciones.conditionals.if_ import If_
from src.instrucciones.funcion.set import Set_
from src.instrucciones.funcion.variable_declaration import VariableDeclaration
from src.instrucciones.usarDB import usarDB
from ..expresiones import binaria
from ..instrucciones.funcion import function_declaration
from src.instrucciones.crearTabla import crearTabla
from src.instrucciones.createdb import createDB
from src.instrucciones.procedure.create_procedure import ProcedureDeclaration
from src.instrucciones.procedure.call_procedure import CallProcedure
from src.instrucciones.procedure.alter_procedure import AlterProcedure
from src.instrucciones.truncate.truncateDB import truncateDB
from src.instrucciones.truncate.truncateTabla import truncateTabla
from src.instrucciones.drop.dropDB import dropDB
from src.instrucciones.drop.dropTabla import dropTable
from src.instrucciones.Alter.alterTable import alterTable
from src.instrucciones.insert.insert import insertInstruccion
from src.instrucciones.update.update import updateInstruccion


from src.ast import (
    Select, FromClause, Table,
    WhereClause, AllColumns, TableColumn,
    AliasSelect, SelectAssign, Program,
    ColumnAssignments, Update, Delete,
    SQLUnaryExpression, SQLBinaryExpression, SQLLogicalExpression
)

from src.funciones import (
    Cas, Concatenar, Contar, Hoy, Substraer, Suma
)


class Visitor(ABC):
    def __init__(self, environment):
        self.environment = environment
        self.correct = True

    def log_error(self, msg, row=0, column=1, lexeme=""):
        self.correct = False
        print(msg, f"ln: {row}, col: {column - 1}")
        self.environment.addError("Semántico", lexeme, msg, row, column - 1)

    def visit(self, node, environment):
        if not self.correct:
            return
        if isinstance(node, SQLUnaryExpression):
            self.visitSQLUnaryExpression(node, environment)
        elif isinstance(node, SQLBinaryExpression):
            self.visitSQLBinaryExpression(node, environment)
        elif isinstance(node, SQLLogicalExpression):
            self.visitSQLLogicalExpression(node, environment)
        elif isinstance(node, binaria.Binaria):
            self.visitBinaria(node, environment)
        elif isinstance(node, Cas):
            self.visitCas(node, environment)
        elif isinstance(node, Concatenar):
            self.visitConcatenar(node, environment)
        elif isinstance(node, Contar):
            self.visitContar(node, environment)
        elif isinstance(node, Hoy):
            self.visitHoy(node, environment)
        elif isinstance(node, Substraer):
            self.visitSubstraer(node, environment)
        elif isinstance(node, Suma):
            self.visitSuma(node, environment)
        elif isinstance(node, crearTabla):
            self.visitCrearTabla(node, environment)
        elif isinstance(node, createDB):
            self.visitCreateDB(node, environment)
        elif isinstance(node, truncateDB):
            self.visitTruncateDB(node, environment)
        elif isinstance(node, truncateTabla):
            self.visitTruncateTabla(node, environment)
        elif isinstance(node, dropDB):
            self.visitDropDB(node, environment)
        elif isinstance(node, dropTable):
            self.visitDropTable(node, environment)
        elif isinstance(node, alterTable):
            self.visitAlterTable(node, environment)
        elif isinstance(node, insertInstruccion):
            self.visitInsertInstruccion(node, environment)
        elif isinstance(node, updateInstruccion):
            self.visitUpdateInstruccion(node, environment)

        elif isinstance(node, binaria.Binaria):
            self.visitLogico(node, environment)

        elif isinstance(node, Primitivo):
            self.visitPrimitivo(node, environment)

        elif isinstance(node, binaria.Binaria):
            self.visitRelacional(node, environment)

        elif isinstance(node, function_declaration.FunctionDeclaration ):
             self.visitFunctionDeclaration(node,environment)    
            
        elif isinstance(node,AlterFunction):
            self.visitAlterFunction(node,environment)
            
        elif isinstance(node,CallFunction):
            return self.visitCallFunction(node,environment)

        elif isinstance(node,Return_):
           return self.visitReturn(node,environment)
                
        elif isinstance(node,Set_):
            self.visitSet(node,environment)
             
        # elif isinstance(node,String_):
            # self.visitString(node,environment)
                # 
        elif isinstance(node,VariableDeclaration):
            self.visitVariableDeclaration(node,environment)
    
        elif isinstance(node, AlterProcedure):
            self.visitAlterProcedure(node, environment)

        elif isinstance(node, CallProcedure):
            self.visitCallProcedure(node,environment)

        elif isinstance(node, ProcedureDeclaration):
            self.visitCreateProcedure(node, environment)

        elif isinstance(node,Else_):
            self.visitElse(node,environment)
             
        elif isinstance(node,ElseIf_):
            self.visitElseIf(node,environment)
            
        elif isinstance(node,If_):
            self.visitIf(node,environment)
            
        # elif isinstance(node,StmIf):
            # self.visitStmIf(node,environment)
                # 
        elif isinstance(node,ElseCase):
            self.visitElseCase(node,environment)
            
        elif isinstance(node,StmCase):
            self.visitStmCase(node,environment)
                
        elif isinstance(node,When):
            self.visitWhen(node,environment)

        elif isinstance(node, usarDB):
            self.visitUsar(node, environment)

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

    def visitUsar(self, node, environment):
        pass

    def visitBinaria(self, node, environment):
        pass

    def visitLogico(self, node, environment):
        pass

    def visitPrimitivo(self, node, environment):
        pass

    def visitRelacional(self, node, environment):
        pass

    def visitFunctionDeclaration(self, node, environment):
        pass

    def visitAlterFunction(self, node, environment):
        pass

    def visitCallFunction(self, node, environment):
        pass

    def visitReturn(self, node, environment):
        pass

    def visitSet(self, node, environment):
        pass

    def visitVariableDeclaration(self, node, environment):
        pass

    def visitAlterProcedure(self, node, environment):
        pass

    def visitCallProcedure(self, node, environment):
        pass

    def visitCreateProcedure(self, node, environment):
        pass

    def visitElse(self, node, environment):
        pass

    def visitElseIf(self, node, environment):
        pass

    def visitIf(self, node, environment):
        pass

    def visitStmIf(self, node, environment):
        pass

    def visitElseCase(self, node, environment):
        pass

    def visitWhen(self, node, environment):
        pass

    def visitStmCase(self, node, environment):
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

    def visitSQLUnaryExpression(self, node, environment):
        pass

    def visitSQLBinaryExpression(self, node, environment):
        pass

    def visitSQLLogicalExpression(self, node, environment):
        pass

    def visitCas(self, node, environment):
        pass

    def visitConcatenar(self, node, environment):
        pass

    def visitContar(self, node, environment):
        pass

    def visitHoy(self, node, environment):
        pass

    def visitSubstraer(self, node, environment):
        pass

    def visitSuma(self, node, environment):
        pass

    def visitCrearTabla(self, node, environment):
        pass

    def visitCreateDB(self, node, environment):
        pass

    def visitTruncateTabla(self, node, environment):
        pass

    def visitTruncateDB(self, node, environment):
        pass

    def visitDropDB(self, node, environment):
        pass

    def visitDropTable(self, node, environment):
        pass

    def visitAlterTable(self, node, environment):
        pass

    def visitInsertInstruccion(self, node, environment):
        pass

    def visitUpdateInstruccion(self, node, environment):
        pass
