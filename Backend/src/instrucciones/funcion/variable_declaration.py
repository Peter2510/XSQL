from src.expresiones.variable import Variable
from src.abstract.abstractas import Abstract

class VariableDeclaration(Abstract):
    def __init__(self, row,column, type_, id_):
        super().__init__(row,column)
        self.type = type_
        self.id = id_

    def accept(self, visitor, environment):
        visitor.visit(self,environment)
        
    def interpretar(self,environment):
        var = Variable()
        var.id = self.id
        var.type = self.type
        value = None
        environment.agregarVariable(var)
        return self
        
