from src.instrucciones.funcion.param_function import FunctionParam
from src.abstract.abstractas import Abstract
from src.ejecucion.environment import Environment

class FunctionDeclaration(Abstract):
    def __init__(self, fila, columna , id, params, type_, body):
        super().__init__(fila,columna)
        self.id = id
        self.params = params
        self.type = type_
        self.body = body
        self.name_for_table = self.get_name_for_table()
        self.table = Environment(f"funcion {id}")
        self.table.returned_type = self.type

    def accept(self, visitor, environment = None):
        for param in self.params:
           param.accept(visitor, self.table)          
        visitor.visit(self,environment)
            
    def interpretar(self, environment):
        print("interpretando funcion declaracion")

    def get_name_for_table(self) -> str:
        func_types = ','.join(str(param.type) for param in self.params)
        return f"{self.id}({func_types})"