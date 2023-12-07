from ..abstract.abstractas import Abstract
from ..manejadorXml import manejo as MANEJADOR
class createDB(Abstract):
    def __init__(self, fila, columna, nombre):
        self.nombre = nombre
        super().__init__(fila, columna)

    def interpretar(self, arbol, tabla):
        ## lo que hace de interfaz regresa el valor
        print("crear base de datos: ",self.nombre.valor)
        nombre = self.nombre.valor;

        if (nombre!=""):
            resultado2 = MANEJADOR.createDatabase(nombre);
            print(resultado2,"<<<")
            if (resultado2 == 0):
                print("si crea la base");
            else:
                print("no crea la base");

        return self.nombre
    
