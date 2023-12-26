from ...abstract.abstractas import Abstract
from ...manejadorXml import manejo, Estructura 
import json
import pandas as pd
class updateInstruccion(Abstract):
    
    def __init__(self, fila, columna, nombreTabla, atributos, parametros):
        self.nombreTabla = nombreTabla
        self.atributos = atributos
        self.parametros = parametros
        super().__init__(fila, columna)

    def accept(self, visitor, environment):
        pass

    def interpretar(self,environment):
        print(self.parametros[1].valor)
        ### mandar a llamar a la estructura
        Estructura.load();

        ## variables de uso
        indiceBaseDatos = 0
        for indice in Estructura.Databases:
            if (indice["name"]==Estructura.nombreActual):
                break
            indiceBaseDatos+=1

        ## ver los datos
        indicesModificar = []
        indiceEspecifico=0
        for elementos in Estructura.Databases[indiceBaseDatos]["tables"]:
             if(elementos['name']== self.nombreTabla):

                print("aaaa", elementos['data']['datos'])
                for datos in elementos['data']['datos']:
                    for key, value in datos.items():
                        if (key ==self.parametros[0]):
                            indicesModificar.append(indiceEspecifico)
                            indiceEspecifico+=1
                        ## busqueda de elementos que sean no nulos y primary key.
                            print( "---", key, value, indiceEspecifico-1)
        
        return "nombre"
        

