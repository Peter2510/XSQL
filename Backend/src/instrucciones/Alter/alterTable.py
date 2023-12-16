
from ...abstract.abstractas import Abstract
import pandas as pd
import os 
from ...manejadorXml import manejo, Estructura, obtener

class alterTable(Abstract):
    def __init__(self, fila, columna, nombre, opcionAlter):
        self.nombre = nombre
        self.opcionAlter = opcionAlter
        super().__init__(fila, columna)

    def interpretar(self,environment):
        nombre = self.nombre
        if (isinstance(self.opcionAlter, list)):
            ## emtpmces es add
            print("add");
            Estructura.alterColumnadd(f'./src/data/xml/{Estructura.nombreActual}.xml',self.nombre,self.opcionAlter[0],self.opcionAlter[1]);
        else:
            ## es drop
            Estructura.alterColumnDrop(f'./src/data/xml/{Estructura.nombreActual}.xml',self.nombre,self.opcionAlter)
            print("drop");





    def accept(self, visitor, environment):
        pass
