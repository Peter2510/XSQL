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

        Estructura.truncateTable(f'./src/data/xml/{Estructura.nombreActual}.xml',self.nombre)




    def accept(self, visitor, environment):
        pass
