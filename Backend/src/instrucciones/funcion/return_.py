from src.abstract.abstractas import Abstract

class Return_(Abstract):
    def __init__(self, row,column, instruction):
        super().__init__(row,column)
        self.instruction = instruction

    def accept(self, visitor, environment):
        visitor.visit(self,environment)
        
    def interpretar(self,environment):
        print("interpretando return")