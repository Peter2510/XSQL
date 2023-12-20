import sys
from src.ejecucion.environment import Environment
from prettytable import PrettyTable

class Ejec(object):
    def __init__(self,queryArray):
        self.queryArray = queryArray
    
    def execute(self, environment):
        if isinstance(self.queryArray,list):
            for item in self.queryArray:
              item.interpretar(environment)
              
               
        
        
            



