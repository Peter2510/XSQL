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

        #Estos "interpretar" se ejecuta primero para obtener el tipo del operando
        #En si solo es para obtener el tipo de dato, no se hace la operación
        izq = self.opIzq.interpretar(environment)
        der = self.opDer.interpretar(environment)
        
        if izq is not None and der is not None:

            self.accept(visitor, environment)
            
            if visitor.correct:
                
                variable = Variable();    
                
                if self.tipoOp == '+':
                    
                    if izq.type == Type.TEXT or der.type == Type.TEXT:
                        variable.type = self.tipo
                        variable.value = str(izq.value) + str(der.value)                    
                        return variable
                                                               
                    elif izq.type == Type.BIT and der.type == Type.BIT:
                        variable.type = self.tipo
                        tmp = bool(izq.value) or bool(der.value)
                        if tmp == True:
                            variable.value = 1
                        else: 
                            variable.value = 0
                        return variable
                    
                    else:
                        variable.type = self.tipo
                        variable.value = izq.value + der.value
                        return variable
                                      
                elif self.tipoOp == '-':
                    
                        variable.type = self.tipo
                        variable.value = izq.value - der.value
                        return variable

                elif self.tipoOp == '*':
                                            
                    if izq.type == Type.BIT and der.type == Type.BIT:
                        variable.type = self.tipo
                        tmp = bool(izq.value) and bool(der.value)
                        if tmp == True:
                            variable.value = 1
                        else: 
                            variable.value = 0
                        return variable
                    
                    elif izq.type == Type.DATE or der.type == Type.DATE:
                        variable.type = self.tipo
                        variable.value = str(izq.value) + str(der.value)
                        return variable
                    
                    elif izq.type == Type.DATETIME or der.type == Type.DATETIME:
                        variable.type = self.tipo
                        variable.value = str(izq.value) + str(der.value)
                        return variable
                    
                    else:    
                        variable.type = self.tipo
                        variable.value = izq.value * der.value
                        return variable

                elif self.tipoOp == '/':
                    
                    if der.value == 0:
                        environment.addError("Semántico","0","No se puede dividir entre 0.", self.fila, self.columna)
                        return None
                                      
                    if izq.type == Type.DATE or der.type == Type.DATE:
                        variable.type = self.tipo
                        variable.value = str(izq.value) + str(der.value)
                        return variable
                    
                    elif izq.type == Type.DATETIME or der.type == Type.DATETIME:
                        variable.type = self.tipo
                        variable.value = str(izq.value) + str(der.value)
                        return variable
                    
                    else:
                        variable.type = self.tipo
                        variable.value = izq.value / der.value
                        return variable    
                    
                elif self.tipoOp == '&&':
                        variable.type = self.tipo
                        tmp = bool(izq.value) and bool(der.value)
                        if tmp == True:
                            variable.value = 1
                        else:
                            variable.value = 0
                        return variable
                    
                elif self.tipoOp == '||':
                        variable.type = self.tipo
                        tmp = bool(izq.value) or bool(der.value)
                        if tmp == True:
                            variable.value = 1
                        else:
                            variable.value = 0
                        return variable

                elif self.tipoOp == '>':
                        variable.type = self.tipo
                        tmp = izq.value > der.value
                        if tmp == True:
                            variable.value = 1
                        else:
                            variable.value = 0
                        return variable
                    
                elif self.tipoOp == '>=':
                        variable.type = self.tipo
                        tmp = izq.value >= der.value
                        if tmp == True:
                            variable.value = 1
                        else:
                            variable.value = 0
                        return variable
                    
                elif self.tipoOp == '<':
                        variable.type = self.tipo
                        tmp = izq.value < der.value
                        if tmp == True:
                            variable.value = 1
                        else:
                            variable.value = 0
                        return variable
                    
                elif self.tipoOp == '<=':
                        variable.type = self.tipo
                        tmp = izq.value <= der.value
                        if tmp == True:
                            variable.value = 1
                        else:
                            variable.value = 0
                        return variable
                    
                elif self.tipoOp == '!=':
                        variable.type = self.tipo
                        tmp = izq.value != der.value
                        if tmp == True:
                            variable.value = 1
                        else:
                            variable.value = 0
                        return variable
                    
                elif self.tipoOp == '==':
                        variable.type = self.tipo
                        tmp = izq.value == der.value
                        if tmp == True:
                            variable.value = 1
                        else:
                            variable.value = 0
                        return variable
                 

        else:
            environment.addError("Semántico","0","Error en la operación.", self.fila, self.columna)
            return None

