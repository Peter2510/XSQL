from ..abstract.abstractas import Abstract
from ..manejadorXml import manejo, Estructura 



class usarDB(Abstract):
    
    def __init__(self, fila, columna, nombre):
        self.nombre = nombre
        super().__init__(fila, columna)

    def accept(self, visitor, environment):
        pass

    def interpretar(self,environment):
        nombre = self.nombre
        Estructura.nombreActual = nombre
        print(Estructura.nombreActual)
        return nombre
