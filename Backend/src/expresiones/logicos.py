

from ..abstract.expresion import Expression

class Logico(Expression):
    def __init__(self, fila, columna, opIzq, opDer, tipoOp):
        super().__init__(fila, columna)
        self.opIzq = opIzq
        self.opDer = opDer
        self.tipoOp = tipoOp
    

    def interpretar(self, environment):
        izq = self.opIzq.interpretar(environment)
        der = self.opDer.interpretar(environment)

        if self.tipoOp == '&&':
            if isinstance(izq, (int, float)) and isinstance(der, (int, float)):
                return retornoValor(izq, der, '==')
            elif isinstance(izq, (str)) and isinstance(der, (str)):
                return retornoValor(izq, der, '==')
            else:
                print("Error semántico: No se pueden comparar los valores.")
                return None
        elif self.tipoOp == '||':
            if isinstance(izq, (int, float)) and isinstance(der, (int, float)):
                return retornoValor(izq, der, '!=')
            elif isinstance(izq, (str)) and isinstance(der, (str)):
                return retornoValor(izq, der, '!=')
            else:
                print("Error semántico: No se pueden comparar(distinto) los valores.")
                return None

    

### seccion para los casteos

def retornoValor(op1, op2, tipoOp):
    if(tipoOp == '=='):
        if (op1 == op2):
            return 1
        else: 
            return 0
    elif(tipoOp == '!='):
        if (op1 != op2):
            return 1
        else: 
            return 0
    elif(tipoOp == '>'):
        if (op1 > op2):
            return 1
        else: 
            return 0
    elif(tipoOp == '<'):
        if (op1 < op2):
            return 1
        else: 
            return 0
    elif(tipoOp == '>='):
        if (op1 >= op2):
            return 1
        else: 
            return 0
    elif(tipoOp == '<='):
        if (op1 <= op2):
            return 1
        else: 
            return 0