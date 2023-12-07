from ..abstract.abstractas import Abstract

class createDB(Abstract):
    def __init__(self, fila, columna, nombre):
        self.nombre = nombre
        super().__init__(fila, columna)

    def interpretar(self, arbol, tabla):
        ## lo que hace de interfaz regresa el valor
        print("crear base de datos: ",self.nombre)
        return self.nombre
    
