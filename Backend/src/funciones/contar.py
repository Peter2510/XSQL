
from ..abstract.funcion import Funcion

from ..manejadorXml import manejo, Estructura 


class Contar(Funcion):
    def __init__(self, fila, columna, tabla):
        super().__init__(fila, columna)
        self.tabla = tabla


    ## no se si le enviamos el tipo de dato asi com date
    def interpretar(self, environment):    
        ### llamar a los xml
        Estructura.load()
        if columna != None:
            if columna == '*':
                print('a')
            else:
                print('a')
    
    def accept(self, visitor, environment):
        pass


