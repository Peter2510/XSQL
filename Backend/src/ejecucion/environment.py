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
        self.record = {}
        self.select_records = []
        self.one_record = False
        if padre is not None:
            for variable in padre:
                self.append(variable)
            self.funciones = padre.funciones
            self.procedimientos = padre.procedimientos

    def addError(self,tipo,token,descripcion,fila,columna):
        self.errors.append(T_error(tipo,token,descripcion,fila,columna))
    
    def getErrores(self):
        return self.errors
               
    def agregarFuncion(self, name, funcion):
        self.funciones[name] = funcion
        
    def actualizarFuncion(self, name, funcion):
        self.funciones.update({name: funcion})

    def existeFuncion(self, name):
        return name in self.funciones

    def cantidadParametrosFuncion(self, name):
        return self.funciones[name].getSizeParameters()

    def tipoFuncion(self, name):
        return self.funciones[name].getType()

    def getFuncion(self, name):
        return self.funciones[name]
               
    def agregarProcedimiento(self, name, procedimiento):
        self.procedimientos[name] = procedimiento
        
    def actualizarProcedimiento(self, name, procedimiento):
        self.procedimientos.update({name: procedimiento})

    def existeProcedimiento(self, name):
        return name in self.procedimientos

    def cantidadParametrosProcedimiento(self, name):
        return self.procedimientos[name].getSizeParameters()

    def getProcedimiento(self, name):
        return self.procedimientos[name]
   
    def agregarVariable(self, variable):
        self.append(variable)

    def getVariable(self, id):
        for variable in self:
            if variable.id == id:
                return variable

    def existeVariable(self, id):
        for variable in self:
            if variable.id == id:
                return True
        return False