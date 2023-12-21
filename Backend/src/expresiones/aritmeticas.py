

from ..abstract.expresion import Expression
class Aritmeticas(Expression):
    def __init__(self, fila, columna, opIzq, opDer, tipoOp, tipo = None):
        super().__init__(fila, columna)
        self.opIzq = opIzq
        self.opDer = opDer
        self.tipoOp = tipoOp
        self.tipo = tipo


    def accept(self, visitor, environment):
        self.opIzq.accept(visitor, environment)
        self.opDer.accept(visitor, environment)
        visitor.visit(self, environment)

    def interpretar(self, environment):
        ## esto es como una funcion que se deriva, asi obtienes los numeros como tal
        from src.visitor import ExpressionsVisitor
        visitor = ExpressionsVisitor(environment)
        self.accept(visitor, environment)
        if not visitor.correct:
             print("Error en visitor dentro de interpretar")

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
