from src.instrucciones.funcion.funcion import Funcion, TablaSimbolos
from src.ejecucion.error import T_error
from src.ejecucion.database import Database
from src.ejecucion.symbol import Symbol
from prettytable import PrettyTable
from src.ejecucion.type import *
from datetime import datetime

class Environment:
       
    def __init__(self, father):
        self.funciones = []
        self.procedimientos = []
        self.errors = []
        self.tables = None

    def addError(self,tipo,token,descripcion,fila,columna):
        self.errors.append(T_error(tipo,token,descripcion,fila,columna))
        
    def agregarFunction(self,nombre,parametros):
        self.funciones.append(Funcion(nombre,parametros,TablaSimbolos("global",None)))
        
    def agregarVariable(self,nombreFuncion,nombreVariable,variable):
        #buscar la funcion e ingresar la variable
        for funcion in self.funciones:
            if nombreFuncion == funcion.nombre:
                funcion.tablaSimbolos.agregarVariable(nombreVariable,variable)
                                        
    def existeVariable(self,nombreFuncion,nombreVariable):
        for funcion in self.funciones:
            if nombreFuncion == funcion.nombre:
                if funcion.tablaSimbolos.existeVariable(nombreVariable):
                    return True
                else:
                    return False
        return False
    
    def existeFunction(self,nombre):
        existe = False
        for funcion in self.funciones:
            if nombre == funcion.nombre:
                return True
        return False
    
    def obtenerFuncion(self,nombre):
        for funcion in self.funciones:
            if nombre == funcion.nombre:
                return funcion
        return None
    
    def obtenerVariable(self,nombreFuncion,nombreVariable):
        for funcion in self.funciones:
            if nombreFuncion == funcion.nombre:
                return funcion.tablaSimbolos.obtenerVariable(nombreVariable)
        return None
        
        