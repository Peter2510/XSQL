from abc import ABC
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
        elif isinstance(node,FunctionDeclaration):
            self.visitFunctionDeclaration(node,environment)
        elif isinstance(node,ProcedureDeclaration):
            self.visitProcedure(node,environment)
        elif isinstance(node, FunctionParam):
            self.visitFunctionParam(node, environment)

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
    
    def visitProcedure(self,node,environment):
        pass

    def visitFunctionParam(self,node,environment):
        pass