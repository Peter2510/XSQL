from src.ejecucion.database import Database
from src.ejecucion.symbol import Symbol
from prettytable import PrettyTable
from src.ejecucion.type import *
from datetime import datetime

class Environment:
    def __init__(self, father):
        self.tablaSimbolos = [] ## funciones, procedimentos  se crea una por cada funcion o procedimiento

    def clearTablaSimbolos(self):
        self.tablaSimbolos = []
        
    def guardarVariable(self,name,tipo,value,father):
        valuee = value
        if tipo == Type.DATE:
           valuee = datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
        self.simbolos.append(Symbol(name,tipo,valuee, father))
        env = self
        while env.father != None:
            env = env.father 
        env.tablaSimbolos.append(Symbol(name,tipo,value, father))

    def guardarVariableins(self,name,tipo,value,father):            
        self.simbolos.append(Symbol(name,tipo,value, father))
        env = self
        while env.father != None:
            env = env.father 
        env.tablaSimbolos.append(Symbol(name,tipo,str(value), father))

    def deleteVariable(self, name):
        env = self
        while env.father != None:
            for i in range(0,len(env.simbolos)):
                if env.simbolos[i].name == name:
                    del env.simbolos[i]
                    break
            env = env.father    

    def vaciarVariables(self):
        env = self
        env.simbolos = []
    
    def buscarVariable(self, name, father):
        env = self
        while env.father != None:
            for i in range(0,len(env.simbolos)):
                if env.simbolos[i].name == name and env.simbolos[i].father == father:
                    return {'value': env.simbolos[i].value , 'tipo':env.simbolos[i].tipo,'name':env.simbolos[i].name}
            env = env.father
        env = self
        while env.father != None:
            for i in range(0,len(env.simbolos)):
                if env.simbolos[i].name == name:
                    return {'value': env.simbolos[i].value , 'tipo':env.simbolos[i].tipo,'name':env.simbolos[i].name}
            env = env.father

        