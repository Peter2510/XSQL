from ..abstract.abstractas import Abstract
from ..manejadorXml import manejo

class crearTabla(Abstract):
    def __init__(self, fila, columna, nombre, listaAtributos):
        self.nombre = nombre
        self.listaAtributos = listaAtributos
        super().__init__(fila, columna)

    def interpretar(self, environment):
        ## lo que hace de interfaz regresa el valor
        print("crear Tabla: ",self.nombre)
        print("con esto: ")
        for i in self.listaAtributos:
            print(i)
        ##create table nombre(id,nombre,precio)
        return self.nombre