from src.expresiones.variable import Variable
from src.ejecucion.type import *
from src.abstract.abstractas import Abstract
from src.visitor.check_expressions_visitor import ExpressionsVisitor


class Binaria(Abstract):
    
    def __init__(self, row, column, opIzq,opDer, tipoOp, tipo = None):
        super().__init__(row, column)
        self.opIzq = opIzq
        self.opDer = opDer
        self.tipoOp = tipoOp
        self.tipo = tipo
        
        
    def accept(self, visitor, environment):
        self.opIzq.accept(visitor, environment)
        self.opDer.accept(visitor, environment)
        visitor.visit(self, environment)

    def interpretar(self, environment):
        
        visitor = ExpressionsVisitor(environment)
        #self.accept(visitor, environment)
        #if not visitor.correct:
             #return None

        izq = self.opIzq.interpretar(environment)
        der = self.opDer.interpretar(environment)
        
        if izq is not None and der is not None:

            self.accept(visitor, environment)
            
            if visitor.correct:
                
                variable = Variable();    
                
                if self.tipoOp == '+':
                    
                    if izq.type == Type.TEXT or der.type == Type.TEXT:
                        variable.type = Type.TEXT
                        variable.value = str(izq.value) + str(der.value)                    
                        print(variable.value)        
                        return variable                                            
                                            
                    elif izq.type == Type.DECIMAL or der.type == Type.DECIMAL:
                        variable.type = Type.DECIMAL
                        variable.value = float(izq.value) + float(der.value)
                        print(variable.value)        
                        return variable
                        
                    elif izq.type == Type.INT or der.type == Type.INT:
                        variable.type = Type.INT
                        variable.value = int(izq.value) + int(der.value)
                        print(variable.value)        
                        return variable
                    
                    
                elif self.tipoOp == '-':
                        return izq - der

                elif self.tipoOp == '*':
                        return izq * der

                elif self.tipoOp == '/':
                        if der == 0:
                            environment.addError("Semántico","0","No se puede dividir entre 0.", self.fila, self.columna)
                            return None
                        return izq / der
        else:
            environment.addError("Semántico","0","Error en la operación.", self.fila, self.columna)
            return None
