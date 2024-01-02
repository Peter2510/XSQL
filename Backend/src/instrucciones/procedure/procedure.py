from src.manejadorXml import Estructura
from src.ast.select import Select


class Procedure():
    def __init__(self,nombre,parametros,instrucciones,tipo,argumentos):
        self.nombre = nombre
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.tipo = tipo
        self.argumentos = argumentos
        
        
    def interpretar(self, environment):
        
        #llamado normal
        if self.tipo == 1:
        
            for parametro in self.parametros:
                parametro.interpretar(environment)
            print("termino de ejecutar parametros procedimiento")

            for instruccion in self.instrucciones:
            
                if isinstance(instruccion,list):
                    for instr in instruccion:
                        if isinstance(instr,Select):
                            Estructura.selectFunciones.append(instr.interpretar(environment))
                        else:
                            instr.interpretar(environment)
                else:
                    if isinstance(instruccion,Select):
                        Estructura.selectFunciones.append(instruccion.interpretar(environment))
                    else:
                        instruccion.interpretar(environment)
        else: 
            ##llamado con variables set        
            for parametro in self.parametros:
                parametro.interpretar(environment)
            print("termino de ejecutar parametros procedimiento")
            
            print("Hacer cambios de valores")

            for instruccion in self.instrucciones:
            
                if isinstance(instruccion,list):
                    for instr in instruccion:
                        if isinstance(instr,Select):
                            Estructura.selectFunciones.append(instr.interpretar(environment))
                        else:
                            instr.interpretar(environment)
                else:
                    if isinstance(instruccion,Select):
                        Estructura.selectFunciones.append(instruccion.interpretar(environment))
                    else:
                        instruccion.interpretar(environment)