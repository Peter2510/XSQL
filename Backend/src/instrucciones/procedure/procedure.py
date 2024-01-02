from src.manejadorXml import Estructura
from src.ast.select import Select
from src.instrucciones.funcion.return_ import Return_


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
                    if isinstance(instr,Select):
                        Estructura.selectFunciones.append(instr.interpretar(environment))
                    else:
                        instr.interpretar(environment)
            else:
                if isinstance(instruccion,Select):
                    Estructura.selectFunciones.append(instruccion.interpretar(environment))
                else:
                    instruccion.interpretar(environment)
                