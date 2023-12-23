class Funcion():
    def __init__(self,nombre,tipo,parametros,instrucciones):
        self.nombre = nombre
        self.tipo = tipo
        self.parametros = parametros
        self.instrucciones = instrucciones
        
    def interpretar(self, environment):
        print(self.nombre,self.tipo,self.parametros,self.instrucciones)