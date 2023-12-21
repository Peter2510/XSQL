from src.expresiones.variable import Variable
from src.ejecucion.type import *
from src.abstract.abstractas import Abstract
from src.visitor.check_expressions_visitor import ExpressionsVisitor


class Negativa(Abstract):
    
    def __init__(self, row, column, instruccion):
        super().__init__(row, column)
        self.instruccion = instruccion
        
    def accept(self, visitor, environment):
        pass
    
    def ejecutar(self, environment):
        value = self.instruccion.ejecutar(environment)
        
        if value is not None:
            variable = Variable()
            variable.type = Type.INT
            variable.value = -value.value
            return variable
        
            
    