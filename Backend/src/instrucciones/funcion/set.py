from src.abstract.abstractas import Abstract

class Set_(Abstract):
    def __init__(self, row,column, id_,value):
        super().__init__(row,column)
        self.id = id_
        self.value = value

    def accept(self, visitor, environment):
        visitor.visit(self,environment)
        
    def interpretar(self,environment):
        print("interpretando set")