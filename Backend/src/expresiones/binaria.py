from src.ejecucion.type import *
from src.abstract.abstractas import Abstract

class Binaria(Abstract):
    
    def __init__(self, row, column, opIzq,opDer, tipoOp):
        
        self.opIzq = opIzq
        self.opDer = opDer
        self.tipoOp = tipoOp
        super().__init__(row, column)
        
    def accept(self, visitor, environment):
        visitor.visit(self, environment)

    def interpretar(self, environment):
        
        izq = self.opIzq.interpretar(environment)
        der = self.opDer.interpretar(environment)

        if(izq == None and der == None):
            
            if self.tipoOp == OperationType.SUMA:
                if isinstance(izq, (int, float)) and isinstance(der, (int, float)):
                    return izq + der
                else:
                    print("Error semántico: No se pueden sumar los valores.")
                    return None
            elif self.tipoOp == '-':
                if isinstance(izq, (int, float)) and isinstance(der, (int, float)):
                    return izq - der
                else:
                    print("Error semántico: No se pueden Restar los valores.")
                    return None

            elif self.tipoOp == '*':
                if isinstance(izq, (int, float)) and isinstance(der, (int, float)):
                    return izq * der
                else:
                    print("Error semántico: No se pueden Multiplicar los valores.")
                    return None
            elif self.tipoOp == '/':

                if isinstance(izq, (int, float)) and isinstance(der, (int, float)):
                    if der == 0:
                        return 'error: sintactico'
                    return izq / der
                else:
                    print("Error semántico: No se pueden dividir los valores.")
                    return None
                return None
        else:
            environment.addError("Semantico", "No puede realizarse la operacion, verifica que los valores esten definidos", self.row, self.column)
            