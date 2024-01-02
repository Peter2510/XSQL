from src.abstract.abstractas import Abstract

class String_(Abstract):
    def __init__(self, row,column, type,size):
        super().__init__(row,column)
        self.type = type
        self.size = size

    def accept(self, visitor, environment):
        visitor.visit(self,environment)
        
    def interpretar(self,environment):
        print("interpretando ind")
        