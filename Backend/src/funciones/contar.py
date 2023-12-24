from ..abstract import Abstract
from src.ejecucion.type import Type


class Contar(Abstract):
    def __init__(self, fila, columna, tabla=None):
        super().__init__(fila, columna)
        self.tabla = tabla
        self.tipo = Type.INT

    def __str__(self):
        return "Contar"

    def accept(self, visitor, environment):
        visitor.visit(self, environment)

    def interpretar(self, environment):
        records = environment.select_records
        return len(records)
