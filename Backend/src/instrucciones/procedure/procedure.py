class Procedure():
    def __init__(self,nombre ,parametros,enviroment,instrucciones):
        self.nombre = nombre
        self.parametros = parametros
        self.enviroment = enviroment
        self.instrucciones = instrucciones
        
    def interpretar(self, environment):
        print("Ejecutar de cada instruccion de procedure",self.nombre)