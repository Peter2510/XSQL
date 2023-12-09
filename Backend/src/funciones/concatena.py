
from ..abstract.funcion import Funcion

class Concatenar(Funcion):
    def __init__(self, fila, columna, opIzq, opDer):
        super().__init__(fila, columna)
        self.opIzq = opIzq
        self.opDer = opDer
    

    def interpretar(self, environment):    
        self.tipoOp = tipoOp

