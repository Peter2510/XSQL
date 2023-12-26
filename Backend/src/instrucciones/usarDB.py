from ..abstract.abstractas import Abstract
from ..manejadorXml import manejo, Estructura 

class usarDB(Abstract):
    
    def __init__(self, fila, columna, nombre):
        self.nombre = nombre
        super().__init__(fila, columna)

    def accept(self, visitor, environment):
        visitor.visit(self,environment)

    def interpretar(self,environment):
        nombre = self.nombre
        Estructura.nombreActual = nombre
        print("CAMBIANDO BASE DE DATOS A: ",nombre)
        return nombre
