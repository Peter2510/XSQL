from src.expresiones.variable import Variable
from src.ejecucion.type import *
from src.abstract.abstractas import Abstract


class Negacion(Abstract):
    
    def __init__(self, row, column, instruccion):
        super().__init__(row, column)
        self.instruccion = instruccion
        self.tipo = None
        
    def accept(self, visitor, environment):
        pass
    
    def interpretar(self, environment):
        tmp = self.instruccion.interpretar(environment)
        if tmp is not None:
            if tmp.type == Type.BIT:
                variable = Variable()
                variable.type = tmp.type
                self.tipo = Type.BIT
                tmpValue = not tmp.value 
                if tmpValue == True:
                    variable.value = 1
                else:
                    variable.value = 0
                return variable
            else:
                environment.addError('Semantico', '!=' ,f'No es posible negar de la expresion de tipo {tmp.type.name}', self.fila, self.columna)
                return None
        
            
    