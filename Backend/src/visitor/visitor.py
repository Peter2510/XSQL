from abc import ABC
from ..expresiones import aritmeticas, logicos, primitivos, relacional


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

    def visitAritmeticas(self, node, environment):
        pass

    def visitLogico(self, node, environment):
        pass

    def visitPrimitivo(self, node, environment):
        pass

    def visitRelacional(self, node, environment):
        pass
