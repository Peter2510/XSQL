from ..abstract.abstractas import Abstract

class Primitivo(Abstract):
    def __init__(self, fila, columna, valor, tipo):
        self.valor = valor
        self.tipo = tipo
        super().__init__(fila, columna)

    def interpretar(self, arbol, tabla):
        print("valor: ",self.valor)
        return self.valor
    
    def getTipo(self):
        return self.tipo
