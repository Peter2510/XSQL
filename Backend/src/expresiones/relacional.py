

from ..abstract.abstractas import Abstract

class Relacional(Abstract):
    def __init__(self, fila, columna, opIzq, opDer, tipoOp):
        super().__init__(fila, columna)
        self.opIzq = opIzq
        self.opDer = opDer
        self.tipoOp = tipoOp
    

    def interpretar(self, arbol, tabla):
        ## esto es como una funcion que se deriva, asi obtienes los numeros como tal
        izq = self.opIzq.interpretar(arbol, tabla)
        der = self.opDer.interpretar(arbol, tabla)
        if self.tipoOp == '==':
            return izq+der
        elif self.tipoOp == '!=':
            return izq-der
        elif self.tipoOp == '>':
            return izq*der
        elif self.tipoOp == '<':
            return izq/der
        elif self.tipoOp == '>=':
            return izq*der
        elif self.tipoOp == '<=':
            return izq*der
        elif self.tipoOp == '&&':
            return izq*der
        elif self.tipoOp == '||':
            return izq*der
        elif self.tipoOp == '!':
            return izq*der