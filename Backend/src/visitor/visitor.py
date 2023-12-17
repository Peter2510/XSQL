from abc import ABC

from src.instrucciones.case.else_case import ElseCase
from src.instrucciones.case.stm_case import StmCase
from src.instrucciones.case.when import When
from src.instrucciones.conditionals.else_ import Else_
from src.instrucciones.conditionals.else_if_ import ElseIf_
from src.instrucciones.conditionals.if_ import If_
from src.instrucciones.conditionals.stm_if import StmIf

from src.instrucciones.funcion.alter_function import AlterFunction
from src.instrucciones.funcion.call_function import CallFunction
from src.instrucciones.funcion.return_ import Return_
from src.instrucciones.funcion.set import Set_
from src.instrucciones.funcion.string_ import String_
from src.instrucciones.funcion.variable_declaration import VariableDeclaration
from src.instrucciones.procedure.alter_procedure import AlterProcedure
from src.instrucciones.procedure.call_procedure import CallProcedure
from ..expresiones import aritmeticas, logicos, primitivos, relacional
from ..instrucciones.funcion.function_declaration import FunctionDeclaration
from ..instrucciones.procedure.create_procedure import ProcedureDeclaration
from ..instrucciones.funcion.param_function import FunctionParam


class Visitor(ABC):
    def __init__(self, environment):
        self.environment = environment
        self.correct = True

    def log_error(self, msg, row = None, column = None):
        print(msg)

    def visit(self, node, environment):
        
        if isinstance(node, aritmeticas.Aritmeticas):
            self.visitAritmeticas(node, environment)
            
        elif isinstance(node, logicos.Logico):
            self.visitLogico(node, environment)
            
        elif isinstance(node, primitivos.Primitivo):
            self.visitPrimitivo(node, environment)
            
        elif isinstance(node, relacional.Relacional):
            self.visitRelacional(node, environment)
            
        elif isinstance(node,AlterFunction):
            self.visitAlterFunction(node,environment)
            
        elif isinstance(node,CallFunction):
            self.visitCallFunction(node,environment)
            
        elif isinstance(node,FunctionDeclaration):
            self.visitFunctionDeclaration(node,environment)
                
        elif isinstance(node,Return_):
            self.visitReturn(node,environment)
                
        elif isinstance(node,Set_):
            self.visitSet(node,environment)
            
        elif isinstance(node,String_):
            self.visitString(node,environment)
                
        elif isinstance(node,VariableDeclaration):
            self.visitVariableDeclaration(node,environment)
                
        elif isinstance(node,AlterProcedure):
            self.visitAlterProcedure(node,environment)
                
        elif isinstance(node,CallProcedure):
            self.visitCallProcedure(node,environment)
                
        elif isinstance(node,ProcedureDeclaration):
            self.visitCreateProcedure(node,environment)
                
        elif isinstance(node,Else_):
            self.visitElse(node,environment)
                
        elif isinstance(node,ElseIf_):
            self.visitElseIF(node,environment)
                
        elif isinstance(node,If_):
            self.visitIf(node,environment)
                
        elif isinstance(node,StmIf):
            self.visitStmIf(node,environment)
                
        elif isinstance(node,ElseCase):
            self.visitElseCase(node,environment)
                
        elif isinstance(node,StmCase):
            self.visitWhen(node,environment)
                
        elif isinstance(node,When):
            self.visitStmCase(node,environment)
            pass
            

    def visitAritmeticas(self, node, environment):
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