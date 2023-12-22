from src.abstract.abstractas import Abstract
from src.manejadorXml import Estructura


class Funcion():
    def __init__(self,nombre ,parametros,enviroment,tablaSimbolos,instrucciones):
        self.nombre = nombre
        self.parametros = parametros
        self.enviroment = enviroment
        self.tablaSimbolos = tablaSimbolos
        self.instrucciones = []
        
    def interpretar(self, environment):
        print("Ejecutar de cada instruccion",self.nombre)