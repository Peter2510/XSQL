
from ..abstract.funcion import Funcion
from datetime import date
from datetime import datetime


class Concatenar(Funcion):
    def __init__(self, fila, columna):
        super().__init__(fila, columna)


    ## no se si le enviamos el tipo de dato asi com date
    def interpretar(self, environment):    
        return datetime.now()

