from src.abstract.abstractas import Abstract

class Set_(Abstract):
    def __init__(self, row,column, id_,value):
        super().__init__(row,column)
        self.id = id_
        self.valor = value

    def accept(self, visitor, environment):
        visitor.visit(self,environment)
        
    def interpretar(self,environment):
        value = self.valor.interpretar(environment)
        variable = environment.getVariable(self.id)
        variable.value = value.value
        return self