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