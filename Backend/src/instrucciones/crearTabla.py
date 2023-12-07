from ..abstract.abstractas import Abstract

class crearTabla(Abstract):
    def __init__(self, fila, columna, nombre, listaAtributos):
        self.nombre = nombre
        self.listaAtributos = listaAtributos
        super().__init__(fila, columna)

    def interpretar(self, arbol, tabla):
        ## lo que hace de interfaz regresa el valor
        print("crear Tabla: ",self.nombre.valor)
        for i in self.listaAtributos:
            print(i.valor)
        return self.nombre
    
