class Procedure():
    def __init__(self,nombre,parametros,instrucciones):
        self.nombre = nombre
        self.parametros = parametros
        self.instrucciones = instrucciones
        
    def interpretar(self, environment):
        
        for parametro in self.parametros:
            parametro.interpretar(environment)
        print("termino de ejecutar parametros procedimiento")
        
        for instruccion in self.instrucciones:
            if isinstance(instruccion,list):
                for instr in instruccion:
                    instr.interpretar(environment)
            else:
                instruccion.interpretar(environment)
                