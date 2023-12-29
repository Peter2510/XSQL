from ...abstract.abstractas import Abstract
from ...manejadorXml import manejo, Estructura 
import json
import pandas as pd
import datetime

class insertInstruccion(Abstract):
    
    def __init__(self, fila, columna, nombreTabla, atributos, parametros):
        self.nombreTabla = nombreTabla
        self.atributos = atributos
        self.parametros = parametros
        super().__init__(fila, columna)

    def accept(self, visitor, environment):
        pass

    def interpretar(self,environment):
        nombre = self.nombreTabla
        nuevosParametros =[]
        nuevosAtributos = []


        ### obtencion de archivps
        Estructura.load();
        indiceBaseDatos = 0
        elementosNoNulos =[]
        tipoElemento = []
        nombresElementos = []
        nombreAtributosPrimarios = []
        cantidadValidaElementos =0
        cantidadValidaElementosGeneral =0
        validaciones = False
        validacionUnicoPrimario = False
        existeTabla= True
        yaSellamoDB = False


        ## ver si ya se llamo a la DB 
        if (Estructura.nombreActual != None):
            yaSellamoDB = True
        

        for indice in Estructura.Databases:
                
            if (indice["name"]==Estructura.nombreActual):
                existeTabla = False
                break
            indiceBaseDatos+=1



        for elementos in Estructura.Databases[indiceBaseDatos]["tables"]:
            if(elementos['name']== self.nombreTabla):
                #print("aaaa", elementos['data']['estructura'])
                for key, value in elementos['data']['estructura'].items():
                    ## todo los elementos 
                    tipoElemento.append(value["caracteristicas"])
                    nombresElementos.append(key)
                    ## busqueda de elementos que sean no nulos y primary key.
                    print(value["caracteristicas"]["Atributo3"]['tipo']['restricciones'], "---", key)
                    if (value["caracteristicas"]["Atributo3"]['tipo']['restricciones']=='1' or
                        value["caracteristicas"]["Atributo2"]['nulidad']=='0'):
                        elementosNoNulos.append(key)
                    ## si es primario
                    if (value["caracteristicas"]["Atributo3"]['tipo']['restricciones']=='1'):
                        nombreAtributosPrimarios.append(key)
                    ## busqueda de parametros  con el mismo nombre
                    for cantidad in range(len(self.parametros)):
                        if (key == self.atributos[cantidad]):
                            print("encontrado", key)
#                            cantidadValidaElementos+=1

        ## vistass
        ## not null
        #### validaciones 

        ## ver si ya se nombro la base de datos 
        if (existeTabla == True):
            environment.addError("Semantico", "" ,f"no existe tabla en la BD", self.fila,self.columna)

        #### ver si son iguales 
        if (len(self.atributos) != len(self.parametros)):
            validaciones = True
            print("Error semantico, no son del mismo tamanio")

        ### determina si lo que viene al menos sean atributos no nulos
        for cantidad in range(len(self.atributos)):
            if (self.atributos[cantidad] in elementosNoNulos):
                print("encontrado", self.atributos[cantidad])
                cantidadValidaElementos+=1
        ### ya despues de ver los no nulos, si viene mas que si lo sean, esten en la tabla
        for cantidad in range(len(self.atributos)):
            if (self.atributos[cantidad] in nombresElementos):
                print("encontrado (puede ser nulo)", self.atributos[cantidad])
                cantidadValidaElementosGeneral+=1


        for valores in nombresElementos:
            print(valores, "<<<<<")

        print(cantidadValidaElementos, len(elementosNoNulos))
        ### forma de comprobar, en base a lo que debe venir
        ### si es menor al arreglo, debe tirar error
        if (cantidadValidaElementos<len(elementosNoNulos)):
            validaciones = True
            print("Error semantico, atributos incompletos no nulos")
        if (cantidadValidaElementosGeneral<len(self.atributos)):
            validaciones = True
            print("Error semantico, atributos incorrectos, hay alguno que no existe en tabla")

        #################
        ###validacion que exista ya la tabla primaria
        for elementos in Estructura.Databases[indiceBaseDatos]["tables"]:
                if(elementos['name']== self.nombreTabla):
                    ### para atributos generales de tabla 
                    for datos in elementos['data']['datos']:
                        indice=0
                        for key, value in datos.items():
                            if key in nombreAtributosPrimarios:
                                for nombreAtributo in self.atributos:
                                    if key == nombreAtributo and value == str(self.parametros[indice]):
                                            validacionUnicoPrimario = True
                                            break
                                    indice+=1



   
        
        #################
        #################
        #################
        ##validacion de primario
        if (validacionUnicoPrimario == False):
            # genearcion de json si todo bien jala el json
            if(validaciones == False):
            #### otra validacion, ir a buscar que correspondan los datos 
            ### para ver el tipo en xml
            ### actualizado problema a ver, que si lo hago en desorden ya no reconoceSS
                validacionTipo = True 
                indiceAtributo =0
                cantidadElementoCorrectos = 0

                for elementos in self.atributos:
                    posicion =0
                    for tipoElementos in nombresElementos:
                        if elementos == tipoElementos:
                            valorCadena = ''
                            print(type(self.parametros[indiceAtributo]), tipoElemento[posicion]['Atributo1']['tipo'])
                            if(isinstance(self.parametros[indiceAtributo], int)):
                                valorCadena = 0
                            elif (isinstance(self.parametros[indiceAtributo], float)):
                                valorCadena = 2
                            elif (isinstance(self.parametros[indiceAtributo], str)):
                                valorCadena = "varchar"
                            elif (isinstance(self.parametros[indiceAtributo], datetime.date)):
                                valorCadena = 3
                            elif (isinstance(self.parametros[indiceAtributo], datetime.datetime)):
                                valorCadena = 4
                            elif (isinstance(self.parametros[indiceAtributo], bit)):
                                valorCadena = 1
                     
                            if (str(valorCadena)== str(tipoElemento[posicion]['Atributo1']['tipo'])):
                                print("encotrado",tipoElemento[posicion]['Atributo1']['tipo'], "---JALO---", indiceAtributo)
                                cantidadElementoCorrectos+=1
                            elif (valorCadena == "varchar"):
                                comprobacion = tipoElemento[posicion]['Atributo1']['tipo'].split("NVARCHAR")
                                print(comprobacion)
                                if (len(comprobacion)==2):
                                    print("encotrado",tipoElemento[posicion]['Atributo1']['tipo'], "---JALO---", indiceAtributo)
                                    cantidadElementoCorrectos+=1
                       
                            break
                        posicion+=1
                    
                    indiceAtributo+=1



                if (cantidadElementoCorrectos == len(self.parametros)):
                    validacionTipo = False

                if (validacionTipo == False ):

                    finAtrinutos = []
                    for atributo, valor in zip(self.atributos, self.parametros):
                        print(atributo, valor)
                        jsonEstructura_data = {
                            'valor': atributo,
                            'nulidad': valor
                        }
                        finAtrinutos.append(jsonEstructura_data)

                    diccionario_combinado = {}
                    for diccionario in finAtrinutos:
                        diccionario_combinado[diccionario['valor']] = diccionario['nulidad']
                    print(diccionario_combinado)
                    print( type(diccionario_combinado))

                    print({'todo': 'bien'})
                ## regresar a antes despues de pruebas
                    Estructura.insertTabla(f"./src/data/xml/{Estructura.nombreActual}.xml", self.nombreTabla, diccionario_combinado)
                else:
                    print({'error': 'Error semantico, tipo de datos para los parametros son incorrectos'})
            else:
                print({'error': 'Error semantico, no concuerda'})
        else:
                print({'error': 'Error semantico, llave primaria ya existente'})

        return {'tipo':'insert'}
        

