from manejadorXml import Estructura
from src.instrucciones.funcion.funcion import Funcion
from src.ejecucion.error import T_error
from src.ejecucion.database import Database
from src.ejecucion.symbol import Symbol
from prettytable import PrettyTable
from src.ejecucion.type import *
from datetime import datetime

class Environment(list):
       
    def __init__(self, padre=None):
        super().__init__()
        self.funciones = {}
        self.procedimientos = {}
        self.errors = []
        self.tables = None
        self.padre = padre

    def addError(self,tipo,token,descripcion,fila,columna):
        self.errors.append(T_error(tipo,token,descripcion,fila,columna))
        
    def getFunciones(self):
        return self.funciones

    def existeFuncion(self, nombreFuncion):
        # nombreBaseActual = Estructura.nombreActual
        # if nombreBaseActual in self.funciones:
        #     return nombreFuncion in self.funciones[nombreBaseActual]
        # else:
        #return nombreFuncion in self.funciones
        pass
    
        
    def agregarFuncion(self, name, funcion):
        self.funciones[name] = funcion
        
    def setFuncion(self, name, funcion):
        self.funciones[name] = funcion
                
    def cantidadParametrosFuncion(self, name):
        return self.funciones[name].getSizeParameters()

    def tipoFuncion(self, name):
        return self.funciones[name].getType()

    def getFuncion(self, name):
        return self.funciones[name]
        
    def getProcedimiento(self):
        return self.procedimientos

    def existeProcedimiento(self, name):
        return name in self.procedimientos
        
    def agregarProcedimiento(self, name, procedimiento):
        self.procedimientos[name] = procedimiento
        
    def setProcedimiento(self, name, procedimiento):
        pass
                
    def cantidadParametrosProcedimiento(self, name):
        return self.procedimientos[name].getSizeParameters()

    def getProcedimiento(self, name):
        return self.procedimientos[name]
    
    "entar a la tabla de simblos"
    