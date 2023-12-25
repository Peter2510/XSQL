class Funcion():
    def __init__(self,nombre,tipo,parametros,instrucciones):
        self.nombre = nombre
        self.tipo = tipo
        self.parametros = parametros
        self.instrucciones = instrucciones
        
    def interpretar(self, environment):
        
        for parametro in self.parametros:
            parametro.interpretar(environment)
        
        for instruccion in self.instrucciones:
            instruccion.interpretar(environment)