
from ..abstract.funcion import Funcion

class Substraer(Funcion):
    def __init__(self, fila, columna, nombreTabla):
        super().__init__(fila, columna)
        self.nombreTabla = nombreTabla
    

    def interpretar(self, environment):    
        self.tipoOp = tipoOp

        ## aaqui cabal mandar a sumar toda la columna

