from src.instrucciones.funcion.funcion import Funcion, TablaSimbolos
from src.ejecucion.error import T_error
from src.ejecucion.database import Database
from src.ejecucion.symbol import Symbol
from prettytable import PrettyTable
from src.ejecucion.type import *
from datetime import datetime

class Environment(list):
       
    def __init__(self, padre=None):
        super().__init__()
        self.funciones = []
        self.procedimientos = []
        self.errors = []
        self.record = {}
        self.select_records = []
        self.one_record = False
        if padre is not None:
            for variable in padre:
                self.append(variable)
            self.setFunciones(padre.getFunciones())
            self.setProcedimientos(padre.getProcedimientos())

    def addError(self,tipo,token,descripcion,fila,columna):
        self.errors.append(T_error(tipo,token,descripcion,fila,columna))
        
    def getFunciones(self):
        return self.funciones
    
    def getProcedimientos(self):
        return self.procedimientos
    
    def agregarFuncion(self, name, funcion):
        self.funciones[name] = funcion

    def existeFuncion(self, name):
        return name in self.funciones

    def cantidadParametros(self, name):
        return self.funciones[name].getSizeParameters()

    def tipoFuncion(self, name):
        return self.funciones[name].getType()

    def getFuncion(self, name):
        return self.funciones[name]
    
    def _add(self, variable):
        self.append(variable)

    def getById(self, id):
        for variable in self:
            if variable.getId() == id:
                return variable
        return None

    def contains(self, id):
        for variable in self:
            if variable.getId() == id:
                return True
        return False
        
        