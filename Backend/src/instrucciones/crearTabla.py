from ..abstract.abstractas import Abstract
from ..manejadorXml import manejo, Estructura, obtener
import json
from enum import Enum

class crearTabla(Abstract):
    def __init__(self, fila, columna, nombre, listaAtributos):
        self.nombre = nombre
        self.listaAtributos = listaAtributos
        super().__init__(fila, columna)

    def interpretar(self, environment):
        ### datos de bandera
        ##hacer validacion con la variable global de Estructura
        print(self.listaAtributos)
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
        
        ## VER SI NO SE REPITE EL NOMBRE DE LA TABLA 
        if (len(Estructura.Databases)> indiceBaseDatos):
            for nombreRepetido in Estructura.Databases[indiceBaseDatos]["tables"]:
                if (nombreRepetido["name"] == self.nombre):
                    nombreTablaRepetido = True
                    print("repetido")
                    environment.addError("Semantico", "" ,f"Esta tabla esta repetida en la BD", self.fila,self.columna)
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
                            environment.addError("Semantico", "" ,f"ya existe nombre de esa tabla", self.fila,self.columna)
                            existeNombre = True
                            return
                    ## si no existe nombre de la tabla genera el ingreso 
                    if (not existeNombre):
                        ## deternina si lo que viene es varchar o un enum
                        tipoAtributo = ''
                        if (isinstance(row[1], Enum) ):
                            tipoAtributo = str(row[1].value)
                        elif(isinstance(row[1], list)):
                            if (isinstance(row[1], Enum) ):
                                tipoAtributo = str(row[1][0].value)
                            else:
                                tipoAtributo = str(row[1][0].value)
                        else:
                            print(row[1], "<<")
                            tipoAtributo = str(row[1].type.name)+f"({str(row[1].size.valor)})"

                        if (isinstance(row[3], list)):
                            ## en dado caso sea pk fk
                            if (isinstance(row[3][1], list)):
                                print(row[3][0], (row[3][1][0]), (row[3][1][1]))
                                json_data = {
                                    'tipo':tipoAtributo,
                                    'nulidad': int(row[2]),
                                    'restricciones': {
                                        'nombreTabla':(row[3][1][0]),
                                        'nombreAtributo':(row[3][1][1])
                                    },
                                    'primariaForanea': (row[3][0])
                                }
                                atributosFinales.append(
                                    {
                                    'nombre': row[0],
                                    'data': json_data      
                                    }
                                )
                            #sino pues si lo obtiene
                            else:
                                json_data = {
                                    'tipo':tipoAtributo,
                                    'nulidad': int(row[2]),
                                    'restricciones': {
                                        'nombreTabla':row[3][0],
                                        'nombreAtributo':row[3][1]
                                    },
                                    'primariaForanea': 2
                                }
                                atributosFinales.append(
                                    {
                                    'nombre': row[0],
                                    'data': json_data      
                                    }
                                )
            
                        else:
                            json_data = {
                                'tipo':tipoAtributo,
                                'nulidad': int(row[2]),
                                'restricciones': int(row[3])  # Convierte '0' a False y cualquier otro valor a True
                            }
                            atributosFinales.append(
                                {
                                'nombre': row[0],
                                'data': json_data      
                                }
                            )

                print("Contenido de atributosFinales:")
                print(type(atributosFinales), atributosFinales)


                valoresTabla = []
                for atributo in atributosFinales:
                    print(atributo)
                    nombre = atributo["nombre"]
                    if nombre in valoresTabla:
                        print(nombre, atributo)
                        atributoRepetido= True
                        environment.addError("Semantico", "" ,f"ya existe un atributo con este nombre en esta tabla como referencia", self.fila,self.columna)

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
            environment.addError("Semantico", "" ,f"no existe la base de datos que hace referencia", self.fila,self.columna)


        return 


    def accept(self, visitor, environment):
        visitor.visit(self, environment)