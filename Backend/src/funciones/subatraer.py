
from src.abstract import Abstract


class Substraer(Abstract):
    def __init__(self, fila, columna, value, start, end):
        super().__init__(fila, columna)
        self.value = value
        self.start = start
        self.end = end

    def accept(self, visitor, environment):
        visitor.visit(self, environment)

    def interpretar(self, environment):
        return self.value[self.start:self.end]
