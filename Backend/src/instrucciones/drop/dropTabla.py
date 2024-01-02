from ...abstract.abstractas import Abstract
from ...manejadorXml import  Estructura 
import os
import xml.etree.ElementTree as ET


class dropTable(Abstract):
    
    def __init__(self, fila, columna, nombre):
        self.nombre = nombre
        super().__init__(fila, columna)

    def interpretar(self,environment):
        Estructura.load();


        ## variables de uso
        indiceBaseDatos = 0
        encontroTabla = False
        for indice in Estructura.Databases:
            if (indice["name"]==Estructura.nombreActual):
                break
            indiceBaseDatos+=1

        for base in Estructura.Databases[indiceBaseDatos]["tables"]:
            for key, value in base['data']['estructura'].items():
                try:
                    print(str(value['caracteristicas']['Atributo3']['nombreTabla']),self.nombre)
                    if(str(value['caracteristicas']['Atributo3']['nombreTabla'])==self.nombre):
                        print(str(value['caracteristicas']['Atributo3']['nombreTabla']),self.nombre)
                        encontroTabla = True
                        break
                except:
                    print('error')



        if (not encontroTabla):   
            print('a')
            nombre = self.nombre
            if os.path.exists(f'./src/data/xml/{Estructura.nombreActual}.xml'):
                tree = ET.parse(f'./src/data/xml/{Estructura.nombreActual}.xml')
                root = tree.getroot()
                for table in root.findall(".//Table[@name='{}']".format(nombre)):
                    root.remove(table)
                tree.write(f'./src/data/xml/{Estructura.nombreActual}.xml')
            else:
                print("No existe la base de datos")
                environment.addError("Semantico", {self.nombre} ,f"no existe la  base de datos",  self.fila, self.columna)

            return {'tipo':'drop', 'mensaje':'se elimino correctamente'}
        else:
            environment.addError("Semantico", {self.nombre} ,f"no se puede eliminar la DB porque depende de otra",  self.fila, self.columna)


    def accept(self, visitor, environment):
        visitor.visit(self, environment)
