from ..abstract import Abstract
from src.ejecucion.type import Type


class Cas(Abstract):
    def __init__(self, fila, columna, expr, new_type):
        super().__init__(fila, columna)
        self.expr = expr
        self.new_type = new_type
        self.tipo = new_type

    def accept(self, visitor, environment):
        self.expr.accept(visitor, environment)
        visitor.visit(self, environment)

    # no se si le enviamos el tipo de dato asi com date
    def interpretar(self, environment):
        return 0
