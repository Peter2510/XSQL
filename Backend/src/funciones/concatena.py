from src.abstract import Abstract
from src.ejecucion.type import Type

class Concatenar(Abstract):
    def __init__(self, fila, columna, opIzq, opDer):
        super().__init__(fila, columna)
        self.opIzq = opIzq
        self.opDer = opDer
        self.tipo = Type.TEXT

    def accept(self, visitor, environment):
        self.opIzq.accept(visitor, environment)
        self.opDer.accept(visitor, environment)
        visitor.visit(self, environment)

    def interpretar(self, environment):
        # return self.opIzq + self.opDer
        return "concatenado"