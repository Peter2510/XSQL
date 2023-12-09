

from ..abstract.expresion import Expression
class Aritmeticas(Expression):
    def __init__(self, fila, columna, opIzq, opDer, tipoOp):
        super().__init__(fila, columna)
        self.opIzq = opIzq
        self.opDer = opDer
        self.tipoOp = tipoOp
    

    def interpretar(self, environment):
        ## esto es como una funcion que se deriva, asi obtienes los numeros como tal
        izq = self.opIzq.interpretar(environment)
        der = self.opDer.interpretar(environment)

        if self.tipoOp == '+':
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
