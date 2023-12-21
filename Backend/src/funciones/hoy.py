
from ..abstract.abstractas import Abstract
from datetime import date
from datetime import datetime
from src.ejecucion.type import Type

class Hoy(Abstract):
    def __init__(self, fila, columna):
        super().__init__(fila, columna)
        self.tipo = Type.DATETIME

    def accept(self, visitor, environment):
        visitor.visit(self, environment)
    # no se si le enviamos el tipo de dato asi com date

    def interpretar(self, environment):
        return datetime.now()
