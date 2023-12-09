
from ..abstract.funcion import Funcion
from datetime import date
from datetime import datetime


class Contar(Funcion):
    def __init__(self, fila, columna, tabla):
        super().__init__(fila, columna)
        self.tabla = tabla


    ## no se si le enviamos el tipo de dato asi com date
    def interpretar(self, environment):    
        return datetime.now()

