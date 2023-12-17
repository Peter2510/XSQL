
from ..abstract import Abstract


class Suma(Abstract):
    def __init__(self, fila, columna, value):
        super().__init__(fila, columna)
        self.value = value

    def accept(self, visitor, environment):
        visitor.visit(self, environment)

    # no se si le enviamos el tipo de dato asi com date
    def interpretar(self, environment):
        return 0
