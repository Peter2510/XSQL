from ..abstract.expresion import Expression

class Primitivo(Expression):
    def __init__(self, fila, columna, valor, tipo):
        self.valor = valor
        self.tipo = tipo
        super().__init__(fila, columna)

    def interpretar(self, environment):
        return self.valor
    
    def getTipo(self):
        return self.tipo
