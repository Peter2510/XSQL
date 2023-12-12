from ..abstract.abstractas import Abstract
from ..manejadorXml import manejo, Estructura, obtener
import json

class crearTabla(Abstract):
    def __init__(self, fila, columna, nombre, listaAtributos):
        self.nombre = nombre
        self.listaAtributos = listaAtributos
        super().__init__(fila, columna)

    def interpretar(self, environment):
        ### datos de bandera
        existeNombre = False
        columnas = []
        ##primero llamo a que me traigan todos los archivos
        Estructura.load();
        ## lo que hace de interfaz regresa el valor
        print("crear Tabla: ",self.nombre)
        print("DBB: ",Estructura.Databases)

        json_data = {}
        atributosFinales = []
        for row in self.listaAtributos:
            json_data = {
                'tipo': row[1],
                'nulidad': int(row[2]),
                'restricciones': bool(row[3])  # Convierte '0' a False y cualquier otro valor a True
            }
            atributosFinales.append(
                {
                'nombre': row[0],
                'data': json_data      
                }
            )
        print("Contenido de atributosFinales:")
        print(type(atributosFinales))



        for atributos in self.listaAtributos:
            print(atributos)
            columnas.append(atributos)

        print("con esto: ")

        json_output = json.dumps(atributosFinales, indent=2)
        print(atributosFinales)
        print("Contenido de json_output:")
        print(type(json_output))

        ## primero determinar si no hay problemas con las filas
  
        
        
        print(columnas)

        if (existeNombre==False):
            print(type(self.listaAtributos))

            valoresTabla = []
            ## para ver si se reptie
            for i in self.listaAtributos:
                for j in i:
                    print(j)
                    
                    ##create table nombre(id,nombre,precio)


        #Estructura.crearTabla("miDB", self.nombre, json_output[0] )
        datos = [
            {
                "nombre": "id",
                "data": {
                    "tipo": "int",
                    "nulidad": 0,
                    "restricciones": True
                }
            },
               {
                "nombre": "id2",
                "data": {
                    "tipo": "var",
                    "nulidad": 0,
                    "restricciones": False
                }
            },
             {
                "nombre": "id3",
                "data": {
                    "tipo": "var",
                    "nulidad": 0,
                    "restricciones": False
                }
            }
            # ... otros datos
        ]

        #obtener.exportDataToXML(datos, "nuevoTabla")
        print(type(datos), type(datos[0]))
        Estructura.crearTabla(Estructura.nombreActual, self.nombre, atributosFinales)

        return self.nombre