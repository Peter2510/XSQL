from src.manejadorXml import Estructura
from src.ast.select import Select
from src.instrucciones.funcion.return_ import Return_


class Funcion():
    def __init__(self,nombre,tipo,parametros,instrucciones):
        self.nombre = nombre
        self.tipo = tipo
        self.parametros = parametros
        self.instrucciones = instrucciones
        
        
    def interpretar(self, environment):
        
        for parametro in self.parametros:
            parametro.interpretar(environment)
        print("termino de ejecutar parametros")
        
        for instruccion in self.instrucciones:
        
            if isinstance(instruccion,list):
                for instr in instruccion:
                    if isinstance(instr,Return_):
                        return instr.interpretar(environment)                    
                    if isinstance(instr,Select):
                        Estructura.selectFunciones.append(instr.interpretar(environment))
                    else:
                        instr.interpretar(environment)
            else:
                if isinstance(instruccion,Return_):
                    return instruccion.interpretar(environment)
                if isinstance(instruccion,Select):
                    Estructura.selectFunciones.append(instruccion.interpretar(environment))
                else:
                    instruccion.interpretar(environment)
                