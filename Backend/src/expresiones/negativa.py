from src.expresiones.variable import Variable
from src.ejecucion.type import *
from src.abstract.abstractas import Abstract


class Negativa(Abstract):
    
    def __init__(self, row, column, instruccion):
        super().__init__(row, column)
        self.instruccion = instruccion
        self.tipo = None
        
    def accept(self, visitor, environment):
        pass
    
    def interpretar(self, environment):
        tmp = self.instruccion.interpretar(environment)
        if tmp is not None:
            variable = Variable()
            if tmp.type == Type.INT or tmp.type == Type.DECIMAL:
                variable.type = tmp.type
                variable.value = tmp.value * -1
                self.tipo = tmp.type
                return variable
            else:
                environment.addError('Semantico', '-' ,f'No es posible el negativo de la expresion de tipo {tmp.type.name}', self.fila, self.columna)
                return None
        
            
    