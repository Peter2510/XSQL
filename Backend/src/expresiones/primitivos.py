from ..abstract.abstractas import Abstract

class primitivos(Abstract):
    def __init__(self, fila, columna, valor, tipo):
        self.valor = valor
        self.tipo = tipo
        super().__init__(fila, columna)

    def interpretar(self, arbol, tabla):
        ## lo que hace de interfaz regresa el valor
        print("valor: ",self.valor)
        return self.valor
    
    def getTipo(self):
        return self.tipo
