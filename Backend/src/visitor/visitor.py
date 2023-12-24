from abc import ABC
from src.instrucciones.conditionals.if_ import If_
from src.instrucciones.funcion.set import Set_
from src.instrucciones.funcion.variable_declaration import VariableDeclaration
from src.instrucciones.usarDB import usarDB
from ..expresiones import binaria
from ..instrucciones.funcion import function_declaration



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

        if isinstance(node, binaria.Binaria):
            self.visitBinaria(node, environment)
            
        elif isinstance(node, binaria.Binaria):
            self.visitLogico(node, environment)
            
        elif isinstance(node, binaria.Binaria):
            self.visitPrimitivo(node, environment)
            
        elif isinstance(node, binaria.Binaria):
            self.visitRelacional(node, environment)

        elif isinstance(node, function_declaration.FunctionDeclaration ):
             self.visitFunctionDeclaration(node,environment)    
            
        # elif isinstance(node,AlterFunction):
            # self.visitAlterFunction(node,environment)
            # 
        # elif isinstance(node,CallFunction):
            # self.visitCallFunction(node,environment)
            # 
            # 
        # elif isinstance(node,Return_):
            # self.visitReturn(node,environment)
                # 
        elif isinstance(node,Set_):
            self.visitSet(node,environment)
             
        # elif isinstance(node,String_):
            # self.visitString(node,environment)
                # 
        elif isinstance(node,VariableDeclaration):
            self.visitVariableDeclaration(node,environment)
    
        # elif isinstance(node,AlterProcedure):
            # self.visitAlterProcedure(node,environment)
                # 
        # elif isinstance(node,CallProcedure):
            # self.visitCallProcedure(node,environment)
                # 
        # elif isinstance(node,ProcedureDeclaration):
            # self.visitCreateProcedure(node,environment)
                # 
        # elif isinstance(node,Else_):
            # self.visitElse(node,environment)
                # 
        # elif isinstance(node,ElseIf_):
            # self.visitElseIF(node,environment)
                # 
        elif isinstance(node,If_):
            self.visitIf(node,environment)
            
        # elif isinstance(node,StmIf):
            # self.visitStmIf(node,environment)
                # 
        # elif isinstance(node,ElseCase):
            # self.visitElseCase(node,environment)
                # 
        # elif isinstance(node,StmCase):
            # self.visitWhen(node,environment)
                # 
        # elif isinstance(node,When):
            # self.visitStmCase(node,environment)

        elif isinstance(node,usarDB):
            self.visitUsar(node,environment)
                   
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

    def visitUsar(self,node,environment):
        pass

    def visitBinaria(self, node, environment):
        pass

    def visitLogico(self, node, environment):
        pass

    def visitPrimitivo(self, node, environment):
        pass

    def visitRelacional(self, node, environment):
        pass
    
    def visitFunctionDeclaration(self,node,environment):
        pass
    
    def visitAlterFunction(self,node,environment):
        pass
    
    def visitCallFunction(self,node,environment):
        pass
    
    def visitReturn(self,node,environment):
        pass
    
    def visitSet(self,node,environment):
        pass
    
    def visitVariableDeclaration(self,node,environment):
        pass
    
    def visitAlterProcedure(self,node,environment):
        pass
    
    def visitCallProcedure(self,node,environment):
        pass
    
    def visitCreateProcedure(self,node,environment):
        pass    
    
    def visitElse(self,node,environment):
        pass
    
    def visitElseIf(self,node,environment):
        pass
    
    def visitIf(self,node,environment):
        pass
    
    def visitStmIf(self,node,environment):
        pass
    
    def visitElseCase(self,node,environment):
        pass
    
    def visitWhen(self,node,environment):
        pass
    
    def visitStmCase(self,node,environment):
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
