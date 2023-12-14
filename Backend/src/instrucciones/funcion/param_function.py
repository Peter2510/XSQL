from src.abstract.abstractas import Abstract

class FunctionParam(Abstract):
    def __init__(self, fila,columna, type_, id_):
        super().__init__(fila,columna)
        self.type = type_
        self.id = id_

    def accept(self, visitor, environment):
        #if environment is not None:
        #    visitor.environment = environment
        #self.id.accept(visitor, environment)
        visitor.visit(self,environment)
        
    def interpretar(self,environment):
        print("interpretando parametro de una funcion")