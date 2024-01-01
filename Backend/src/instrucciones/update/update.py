from ...abstract.abstractas import Abstract
from ...manejadorXml import manejo, Estructura 
from ...ast.sql_expression import SQLUnaryExpression, SQLBinaryExpression

import json
import pandas as pd
class updateInstruccion(Abstract):
    
    def __init__(self, fila, columna, nombreTabla, atributos, parametros):
        self.nombreTabla = nombreTabla
        self.atributos = atributos
        self.parametros = parametros
        super().__init__(fila, columna)

    def accept(self, visitor, environment):
        visitor.visit(self, environment)

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
                                if (self.parametros[0] == key and str(self.parametros[1]) == value):
                            ## busqueda de elementos que sean no nulos y primary key.
                                    indicesModificar.append(indicesIdeales)
                                    print( "---", key, value, indiceEspecifico-1, indicesIdeales)
                        
                        indicesIdeales+=1


            ### obtencion de los parametros
            valoresAtributosTS = []
            diccionarioAtributos = {}
            diccionarioAtributos["parametros"] = []
            indiceAtributo = 0
            for nombre in self.atributos:
                if isinstance(nombre[1], (SQLUnaryExpression, SQLBinaryExpression)):
                    #buscar todos los valores que no sean simples cadenas
                    if hasattr(nombre[1], 'valor'):
                        if (nombre[1].valor == None):
                            print((nombre[1]))
                            valor_parametro = nombre[1].valor
                            print(valor_parametro)
                            valoreIndividual = str(nombre[1]).split(' ');
                            diccionarioIndividual = {}
                            diccionarioIndividual["valores"] = []
                            for valor in valoreIndividual:
                                #print(valor.replace("None.", ""),"<><>")
                                diccionarioIndividual["valores"].append(valor.replace("None.", "\\"))
                            
                            diccionarioAtributos["parametros"].append( diccionarioIndividual)
                    else:
                        print("No se pudo encontrar el valor del parámetro.")


            ## ahora con el ciclo que busque cuales son iguales en la primera
            ## casilla con // y mire si hay algun valor con algun valor antes y lo cambie
            ### sino de una que tire error
            for nombresParametros in self.atributos:
                indiceValoresReferenciados = 0
                for nombresDiccionario in diccionarioAtributos["parametros"]:
                    indiceAtributoEncontrado =0
                    for nombreIndividualDiccionario in nombresDiccionario["valores"]:
                        if(nombreIndividualDiccionario.startswith( "\\")
                        and nombreIndividualDiccionario.replace( "\\", "") ==nombresParametros[0]):
                                print(nombresParametros[0],nombreIndividualDiccionario)
                                if (nombresParametros[1].tipo != None):
                                    print("si distinto", nombresParametros[1].tipo, nombresParametros[1])

                                    ## ver bien eso del tipo
                                    diccionarioAtributos["parametros"][indiceValoresReferenciados]["valores"][indiceAtributoEncontrado]=(nombresParametros[1])
                        indiceAtributoEncontrado+=1


            print(diccionarioAtributos["parametros"][0]["valores"][2], diccionarioAtributos)





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

                        ### aqui cada nombre le debo de enviar su parametro
                        ### esto en base a lo que genere arriba
                        ## en dado caso haya uno que se construya con otro 
                        ### no deberia haber problema porque deberian de ser
                        ## del mismo tamanio
                        for nombrePeticion in self.atributos:
                            if (datos == nombrePeticion[0]):
                                nombresElementosEncontrados.append(datos)
                                elementosaCambiar.append(nombrePeticion[1])
                                elementos['data']['datos'][indices][f'{datos}'] = nombrePeticion[1]
                                elementosEncontrados.append( elementos['data']['datos'][indices][f'{datos}'])
                                print('si esta ', datos,nombrePeticion[1],elementos['data']['datos'][indices] )
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

            for nombresIndividual in nombresCompletos:
                print(nombresIndividual) 



            ###validacion
            if (cantidadElementosPeticion < len(self.atributos)):
                esValido = False


            if (esValido):
                ### generacion grupal CREACION GENERAL Y ELIMINACION DE TODo 
                ### truncar todo
                #SEstructura.truncateTable(f'./src/data/xml/{Estructura.nombreActual}.xml',self.nombreTabla)

                ### ciclo para ingresar todo:
                #for diccionario in (nombresCompletos):
                   # Estructura.insertTabla(f"./src/data/xml/{Estructura.nombreActual}.xml", self.nombreTabla, diccionario)
                print("volver a quitar el comentario")
            else: 
                print({'error':'error semantico, atributos no existen en la base de datos'})

            ## solo para prueba de ingreso
            #Estructura.insertTabla(f"./src/data/xml/{Estructura.nombreActual}.xml", self.nombreTabla, diccionario_combinado)

        else:  
                print({'error':'no existe la tabla en la DB'})
        return "nombre"
        

