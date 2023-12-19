
from ..abstract import Abstract


class Contar(Abstract):
    def __init__(self, fila, columna, tabla = None):
        super().__init__(fila, columna)
        self.tabla = tabla

    def accept(self, visitor, environment):
        visitor.visit(self, environment)

    # no se si le enviamos el tipo de dato asi com date
    def interpretar(self, environment):
        return 0
