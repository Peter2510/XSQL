import sys
from src.manejadorXml import Estructura
from src.ejecucion.environment import Environment
from prettytable import PrettyTable

class Ejec(object):
    def __init__(self,queryArray):
        self.queryArray = queryArray
        self.valores = []
    
    def execute(self, environment):
        if isinstance(self.queryArray,list):
            for item in self.queryArray:
                self.valores.append(item.interpretar(environment))
            for i in Estructura.selectFunciones:
                self.valores.append(i)
            Estructura.selectFunciones=[]
                
        return [valor for valor in self.valores if valor is not None]