from ..abstract.abstractas import Abstract
from ..manejadorXml import manejo, Estructura, obtener
import json

class crearTabla(Abstract):
    def __init__(self, fila, columna, nombre, listaAtributos):
        self.nombre = nombre
        self.listaAtributos = listaAtributos
        super().__init__(fila, columna)

    def interpretar(self, tablaSimbolos):
        ### datos de bandera
        ##hacer validacion con la variable global de Estructura
        existeNombre = False
        nombreTablaRepetido = False
        atributoRepetido = False

        columnas = []
        indiceBaseDatos = 0

        ##primero llamo a que me traigan todos los archivos
        Estructura.load();
        for indice in Estructura.Databases:
            if (indice["name"]==Estructura.nombreActual):
                break
            indiceBaseDatos+=1
        print("---------------------------------------------------------------",Estructura.Databases[0]["tables"],"----------")
        
        ## VER SI NO SE REPITE EL NOMBRE DE LA TABLA 
        if (len(Estructura.Databases)> indiceBaseDatos):
            for nombreRepetido in Estructura.Databases[indiceBaseDatos]["tables"]:
                if (nombreRepetido["name"] == self.nombre):
                    nombreTablaRepetido = True
                    print("repetido")
                    break

            if (nombreTablaRepetido == False):
                ## lo que hace de interfaz regresa el valor
                print("crear Tabla: ",self.nombre)
                ##creacion de la forma que tenemos para las tablas
                json_data = {}
                atributosFinales = []
                for row in self.listaAtributos:
                    ## primero ver si no hay repetidos
                    for valoresRepetidos in columnas:
                        if (row[0] != valoresRepetidos):
                            valoresRepetidos.append(row[0])
                        else:
                            print({"error": 'error semantico, ya existe nombre de esa tabla'})
                            existeNombre = True
                            return
                    ## si no existe nombre de la tabla genera el ingreso 
                    if (not existeNombre):
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


                valoresTabla = []
                for atributo in atributosFinales:
                    nombre = atributo["nombre"]
                    if nombre in valoresTabla:
                        atributoRepetido= True
                        print({"error": 'Error semántico, ya existe un atributo con este nombre en esta tabla como referencia'})
                        break
                    else:
                        valoresTabla.append(nombre)

                ## ver que no se repitan los nombres de los atributos


                ## primero determinar si no hay problemas con las filas
                #if (existeNombre==False):
                 #   valoresTabla = []
                    ## para ver si se reptie
           
                            ## CREACION FINAL
                if(atributoRepetido == False):
                   Estructura.crearTabla(Estructura.nombreActual, self.nombre, atributosFinales)
        else:
            print({"error": 'error semantico, no existe la base de datos que hace referencia'})


        return self.nombre


    def accept(self, visitor, environment):
        pass
