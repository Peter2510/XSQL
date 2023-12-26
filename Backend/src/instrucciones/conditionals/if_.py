from src.abstract.abstractas import Abstract


class If_(Abstract):
    
    def __init__(self, row, column,condition, instructions):
        super().__init__(row,column)
        self.condition = condition
        self.instructions = instructions
        
        
    def accept(self, visitor, environment):
        visitor.visit(self,environment)
        
    def interpretar(self, environment):
        print("interpretando if")
        