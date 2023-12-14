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
            print("No existe la base de datos")
        return nombre

