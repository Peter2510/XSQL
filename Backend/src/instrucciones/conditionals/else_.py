from src.abstract.abstractas import Abstract


class Else_(Abstract):
    
    def __init__(self, row, column, instructions):
        super().__init__(row,column)
        self.instructions = instructions
        
        
    def accept(self, visitor, environment):
        visitor.visit(self, environment)
        
    def interpretar(self, environment):
        print("interpretando else")
        