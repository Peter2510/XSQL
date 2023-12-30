from src.abstract.abstractas import Abstract


class Else_(Abstract):
    
    def __init__(self, row, column, instructions):
        super().__init__(row,column)
        self.instructions = instructions
        
        
    def accept(self, visitor, environment):
        visitor.visit(self, environment)
        
    def interpretar(self, environment):
        for i in self.instructions:
            if isinstance(i,list):
                for j in i:
                    j.interpretar(environment)
            else:
                i.interpretar(environment)
        