from ...abstract.abstractas import Abstract
from ...manejadorXml import manejo, Estructura 
import json
import pandas as pd
class insertInstruccion(Abstract):
    
    def __init__(self, fila, columna, nombreTabla, atributos, parametros):
        self.nombreTabla = nombreTabla
        self.atributos = atributos
        self.parametros = parametros
        super().__init__(fila, columna)

    def accept(self, visitor, environment):
        pass

    def interpretar(self,environment):
        nombre = self.nombreTabla
        nuevosParametros =[]
        nuevosAtributos = []
        
        # genearcion de json
        finAtrinutos = []
        for atributo, valor in zip(self.atributos, self.parametros):
            json_data = {
                'valor': atributo,
                'nulidad': valor
            }
            finAtrinutos.append(json_data)
        diccionario_combinado = {}

        for diccionario in finAtrinutos:
            diccionario_combinado[diccionario['valor']] = diccionario['nulidad']
        print(diccionario_combinado)
        print( type(diccionario_combinado))

        Estructura.insertTabla(f"./src/data/xml/{Estructura.nombreActual}.xml", self.nombreTabla, diccionario_combinado)
        print(self.nombreTabla, self.parametros)
        return nombre
        

