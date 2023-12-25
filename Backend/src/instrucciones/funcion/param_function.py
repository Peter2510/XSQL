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
        var.value = None
        environment.agregarVariable(var)
        
    def get_row(self):
        return self.row

    def get_column(self):
        return self.column