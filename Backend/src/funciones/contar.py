from ..abstract import Abstract
from src.ejecucion.type import Type

class Contar(Abstract):
    def __init__(self, fila, columna, tabla = None):
        super().__init__(fila, columna)
        self.tabla = tabla
        self.tipo = Type.INT

    def accept(self, visitor, environment):
        visitor.visit(self, environment)

    # no se si le enviamos el tipo de dato asi com date
    def interpretar(self, environment):
        return 0
