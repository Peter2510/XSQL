from ..abstract.abstractas import Abstract
from ..manejadorXml import manejo, Estructura 


class crearTabla(Abstract):
    def __init__(self, fila, columna, nombre, listaAtributos):
        self.nombre = nombre
        self.listaAtributos = listaAtributos
        super().__init__(fila, columna)

    def interpretar(self, environment):
        ### datos de bandera
        existeNombre = False
        ##primero llamo a que me traigan todos los archivos
        Estructura.load();
        ## lo que hace de interfaz regresa el valor
        print("crear Tabla: ",self.nombre)
        print("con esto: ")
        ## primero determinar si no hay problemas con las filas
        for i in Estructura.Databases:
            for j in i["tables"]:
                print(j["name"])
                if (self.nombre == j["name"]):
                    existeNombre = True
                    return True
    

        if (existeNombre==False):
            print(type(self.listaAtributos))
            valoresTabla = []
            ## para ver si se reptie
            for i in self.listaAtributos:
                    if i in valoresTabla:
                        print("Error semantico tablas repetidas")
                        return True
                    valoresTabla.append(i)
                    print(i)
            print(valoresTabla)
                    ##create table nombre(id,nombre,precio)
        Estructura.crearTabla("miDB", "empleados", {
            "id": "INTEGER",
            "nombre": "VARCHAR(50)",
            "edad": "BIGINT"
         
        })

        return self.nombre