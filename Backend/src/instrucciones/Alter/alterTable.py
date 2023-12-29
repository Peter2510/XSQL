
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
            ## varibles de uso
            columnasExistentes = []
            indiceBaseDatos =0
            sinProblemaAlter = False
            ## emtpmces es add
            print("add");
            Estructura.load()
            for indice in Estructura.Databases:
                if (indice["name"]==Estructura.nombreActual):
                    break
                indiceBaseDatos+=1
            ## solo buscar si hay ya elementos nuevos
            #print("forma:dddddddd",Estructura.Databases[indiceBaseDatos]["tables"][0]["data"]["estructura"]["idfactura"])
            if (len(Estructura.Databases)> indiceBaseDatos):
                for nombres in Estructura.Databases[indiceBaseDatos]["tables"]:
                   # print(">>>>>>>",nombres["data"]["estructura"])
                    for valoresNombreRepetidos in nombres["data"]["estructura"]:
                        if valoresNombreRepetidos == self.opcionAlter[0]:
                            sinProblemaAlter = True
                            break

            if (not sinProblemaAlter):
                Estructura.alterColumnadd(f'./src/data/xml/{Estructura.nombreActual}.xml',self.nombre,self.opcionAlter[0],self.opcionAlter[1].value);
            else:
                environment.addError("Semantico", {self.nombre} ,f"ERROR SEMANTICO, existe ya la columna",  self.fila, self.columna)
                print({'error': 'ERROR SEMANTICO, existe ya la columna '})
        else:
            ## es drop
             ## varibles de uso
            columnasExistentes = []
            indiceBaseDatos =0
            sinProblemaAlter = False
            existenDatosReferenciados = 0

            Estructura.load()
            for indice in Estructura.Databases:
                if (indice["name"]==Estructura.nombreActual):
                    break
                indiceBaseDatos+=1
            ## solo buscar si hay ya elementos nuevos
            #print("forma:dddddddd",Estructura.Databases[indiceBaseDatos]["tables"][0]["data"]["estructura"]["idfactura"])
            if (len(Estructura.Databases)> indiceBaseDatos):
                for nombres in Estructura.Databases[indiceBaseDatos]["tables"]:
                   # print(">>>>>>>",nombres["data"]["estructura"])
                   if (self.nombre == nombres['name']):
                        for valoresNombreRepetidos in nombres["data"]["estructura"]:
                            if valoresNombreRepetidos == self.opcionAlter:
                                sinProblemaAlter = True
                                break
                        for atributosEnUso in nombres["data"]["datos"]:

                            try:
                                if (atributosEnUso[f'{self.opcionAlter}']):
                                    existenDatosReferenciados+=1
                                    break

                            except:
                                print('error, no hay datos')

            if (sinProblemaAlter and existenDatosReferenciados ==0):
                print("drop");
                Estructura.alterColumnDrop(f'./src/data/xml/{Estructura.nombreActual}.xml',self.nombre,self.opcionAlter)
            else:
                if (existenDatosReferenciados!=0):
                    environment.addError("Semantico", {self.nombre} ,f"haya datos que dependen de la columna",  self.fila, self.columna)
                else:
                    print({'error': 'ERROR SEMANTICO, no existe la columna '} )
                    environment.addError("Semantico", {self.nombre} ,f"no existe la columna",  self.fila, self.columna)




    def accept(self, visitor, environment):
        visitor.visit(self, environment)
