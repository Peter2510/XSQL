from ...abstract.abstractas import Abstract
import pandas as pd
import os 
from ...manejadorXml import manejo, Estructura, obtener

class truncateTabla(Abstract):
    
    def __init__(self, fila, columna, nombre):
        self.nombre = nombre
        super().__init__(fila, columna)

    def interpretar(self,environment):
        nombre = self.nombre
        if (Estructura.nombreActual != None):
            Estructura.truncateTable(f'./src/data/xml/{Estructura.nombreActual}.xml',self.nombre)
        else:
            print({'Error': 'error semantico - no se seleccion DB'})



    def accept(self, visitor, environment):
        pass
