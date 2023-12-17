
from src.abstract import Abstract


class Concatenar(Abstract):
    def __init__(self, fila, columna, opIzq, opDer):
        super().__init__(fila, columna)
        self.opIzq = opIzq
        self.opDer = opDer

    def accept(self, visitor, environment):
        visitor.visit(self, environment)

    def interpretar(self, environment):
        return self.opIzq + self.opDer
