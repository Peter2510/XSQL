from src.ejecucion.type import Type
from src.expresiones.variable import Variable
from src.abstract.abstractas import Abstract

class FunctionParam(Abstract):
    def __init__(self, row,column, type_, id_):
        super().__init__(row,column)
        self.type = type_
        self.id = id_

    def accept(self, visitor, environment):
        pass
        
    def interpretar(self,environment):
        print("interpretando parametro de una funcion")
        var = Variable()
        var.type = self.type
        var.id = self.id
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
        
    def get_row(self):
        return self.row

    def get_column(self):
        return self.column