
from ..abstract import Abstract


class Cas(Abstract):
    def __init__(self, fila, columna, expr, new_type):
        super().__init__(fila, columna)
        self.expr = expr  # TODO: expr debería ser un nodo y es necesario validar variables
        self.new_type = new_type

    def accept(self, visitor, environment):
        self.expr.accept(visitor, environment)
        visitor.visit(self, environment)

    # no se si le enviamos el tipo de dato asi com date
    def interpretar(self, environment):
        return 0
