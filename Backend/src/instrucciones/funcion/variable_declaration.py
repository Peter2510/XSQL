from src.ejecucion.type import Type
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
        if self.type == Type.INT:
            var.value = 0        
        elif self.type == Type.DECIMAL:
            var.value = 0.0
        elif self.type == Type.TEXT:
            var.value = ""
        elif self.type == Type.BIT:
            var.value = False
        elif self.type == Type.DATE:
            var.value = "1999-01-01"
        elif self.type == Type.DATETIME:
            var.value = "1999-01-01 00:00:00"
        elif self.type == Type.NULL:
            var.value = ""
        environment.agregarVariable(var)
        
        
