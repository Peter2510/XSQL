from src.abstract.abstractas import Abstract
from src.ejecucion.environment import Environment

class FunctionDeclaration(Abstract):
    def __init__(self, row, column , id, params, type_, body):
        super().__init__(row,column)
        self.id = id
        self.params = params
        self.type = type_
        self.body = body

    def accept(self, visitor, environment):
        visitor.visit(self, environment)
        
    def interpretar(self, environment):
        #guardar la funcion en el environment
        environment
        
        

    def get_name_for_table(self) -> str:
        func_types = ','.join(str(param.type) for param in self.params)
        return f"{self.id}({func_types})"