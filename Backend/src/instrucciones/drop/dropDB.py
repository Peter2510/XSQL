from ...abstract.abstractas import Abstract
import os


class dropDB(Abstract):
    
    def __init__(self, fila, columna, nombre):
        self.nombre = nombre
        super().__init__(fila, columna)

    def interpretar(self,environment):
        nombre = self.nombre
        if os.path.exists(f'./src/data/xml/{nombre}.xml'):
            os.remove(f'./src/data/xml/{nombre}.xml')
        else:
            environment.addError("Semantico", {self.nombre} ,f"no existe la  base de datos",  self.fila, self.columna)
            print("No existe la base de datos")
        return nombre

    def accept(self, visitor, environment):
        pass
