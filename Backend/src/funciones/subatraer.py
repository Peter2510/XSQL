from src.abstract import Abstract
from src.ejecucion.type import Type


class Substraer(Abstract):
    def __init__(self, fila, columna, value, start, end):
        super().__init__(fila, columna)
        self.value = value
        self.start = start
        self.end = end
        self.tipo = Type.TEXT

    def __str__(self):
        return 'SUBSTRAER'

    def accept(self, visitor, environment):
        self.value.accept(visitor, environment)
        visitor.visit(self, environment)

    def interpretar(self, environment):
        result = self.value.interpretar(environment)
        return result[self.start:self.end]
