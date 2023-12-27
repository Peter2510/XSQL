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


        ### mandar a llamar a la estructura
        Estructura.load();
        

        ## variables de uso
        indiceBaseDatos = 0
        encontroTabla = False
        for indice in Estructura.Databases:
            if (indice["name"]==Estructura.nombreActual):
                break
            indiceBaseDatos+=1

        ## ver los datos
        indicesModificar = []
        indicesRestantes = []
        nombresGlobalesdeAtributos = []
        cantidadElementosPeticion = 0
        indiceEspecifico=0


        ## para las validaciones
        esValido = True
        ## ver si existe la tabla en base de datos:
        for elementos in Estructura.Databases[indiceBaseDatos]["tables"]:
            if(elementos['name']== self.nombreTabla):
                encontroTabla = True
                break

        if (encontroTabla):
            for elementos in Estructura.Databases[indiceBaseDatos]["tables"]:
                if(elementos['name']== self.nombreTabla):
                    ### aqui es recorrer e ingresar los indices que cumplen
                    indicesIdeales = 0
                    ### para atributos generales de tabla 
                    for key, value in elementos['data']['estructura'].items():
                            nombresGlobalesdeAtributos.append(key)

                    for datos in elementos['data']['datos']:
                        ### general de indices 
                        indicesRestantes.append(indicesIdeales)

                        for key, value in datos.items():
                                indiceEspecifico+=1
                                if (self.parametros[0] == key and str(self.parametros[1].valor) == value):
                            ## busqueda de elementos que sean no nulos y primary key.
                                    indicesModificar.append(indicesIdeales)
                                    print( "---", key, value, indiceEspecifico-1, indicesIdeales)
                        
                        indicesIdeales+=1

                ### como validacion ir a ver si estan todos los atributos
            for nombreAtributo in self.atributos:
                if nombreAtributo[0] in nombresGlobalesdeAtributos:
                    cantidadElementosPeticion+=1
             ##############           
             ##############           
            ###luego ir a buscar los elementos a modificar
            ## ingreso los elementos que encontro

            ## prueba general todos los datos
            nombresCompletos = []
            datosCompletos = []

            elementosEncontrados = []
            nombresElementosEncontrados = []
            elementosaCambiar = []
            cantidadIgualElementos=0
            for indices in indicesModificar:
                for elementos in Estructura.Databases[indiceBaseDatos]["tables"]:
                 if(elementos['name']== self.nombreTabla):
                    for datos in elementos['data']['datos'][indices]:
                        datosCompletos.append(elementos['data']['datos'][indices][f'{datos}'])
                        for nombrePeticion in self.atributos:
                            if (datos == nombrePeticion[0]):
                                nombresElementosEncontrados.append(datos)
                                elementosaCambiar.append(nombrePeticion[1].valor)
                                elementos['data']['datos'][indices][f'{datos}'] = nombrePeticion[1].valor
                                elementosEncontrados.append( elementos['data']['datos'][indices][f'{datos}'])
                                print('si esta ', datos,nombrePeticion[1].valor,elementos['data']['datos'][indices] )
                        print("ccc",datos,nombrePeticion[0])

                    print("bbb", elementos['data']['datos'][indices])
                    nombresCompletos.append( elementos['data']['datos'][indices])


            ## sino son iguales ir a buscar los que no son indices 
            for indices in indicesRestantes:
                if not indices in indicesModificar:
                    for elementos in Estructura.Databases[indiceBaseDatos]["tables"]:
                        if(elementos['name']== self.nombreTabla):
                            nombresCompletos.append( elementos['data']['datos'][indices])

       
       
       
       
       
            ## aqui mejor buscar bien ingresado el tipo de dato
            for elementosCambiar in elementosEncontrados:
                print(elementosCambiar)
            ### ir a buscar que los elemenentos esten acorde a lo que viene e ingresar
            for nombresIndividual in nombresElementosEncontrados:
                print(nombresIndividual) 
            for nombresIndividual in elementosaCambiar:
                print(nombresIndividual) 
            for nombresIndividual in nombresCompletos:
                print(nombresIndividual) 



            ###validacion
            if (cantidadElementosPeticion < len(self.atributos)):
                esValido = False


            if (esValido):
                ### generacion grupal CREACION GENERAL Y ELIMINACION DE TODo 
                ## estos son de 
                finAtrinutos = []
                for atributo in zip(self.atributos):
                    jsonEstructura_data = {
                            'nombre': atributo[0][0],
                            "tipo":atributo[0][1].valor
                        }
                    finAtrinutos.append(jsonEstructura_data)

                diccionario_combinado = {}
                for diccionario in finAtrinutos:
                        diccionario_combinado[diccionario['nombre']] = diccionario['tipo']
                print("a>>", diccionario_combinado)
                print( type(diccionario_combinado))


                ### truncar todo
                Estructura.truncateTable(f'./src/data/xml/{Estructura.nombreActual}.xml',self.nombreTabla)

                ### ciclo para ingresar todo:
                for diccionario in (nombresCompletos):
                    Estructura.insertTabla(f"./src/data/xml/{Estructura.nombreActual}.xml", self.nombreTabla, diccionario)

            else: 
                print({'error':'error semantico, atributos no existen en la base de datos'})

            ## solo para prueba de ingreso
            #Estructura.insertTabla(f"./src/data/xml/{Estructura.nombreActual}.xml", self.nombreTabla, diccionario_combinado)

        else:  
                print({'error':'no existe la tabla en la DB'})
        return "nombre"
        

