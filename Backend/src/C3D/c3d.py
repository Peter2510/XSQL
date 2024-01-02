
class Nodo:
        def __init__(self, etiqueta, valor = '', hijos = [], fila = -1, columna = -1,  codigo3d = ''):
            self.etiqueta = etiqueta
            self.valor = valor
            self.hijos = hijos
            self.fila = fila
            self.columna = columna
            self.codigo3d = codigo3d

class paraProcedimientos:
    def __init__(self, temporal):
        self.temporal = temporal
    

    def generarTemporal(self):
        t = f't_{str(self.temporal)}'
        self.temporal+=1
        return t

    def ingresoCodigo(self, valor, temporal):
        if isinstance(temporal, str):
            cd3 = '\t'+ valor + " = " + temval
        else:
            cd3 = '\t'+ valor + " = " + str(temval)
        self.codigo3d.append(cd3)
        

        ## para primitivos 

        def getValoresNumeros(t):
            if isinstance(t[1], float):
                gramatica = '<cualquiernumero> ::= \"'+str(t[1])+'\"'
                return Nodo('DECIMAL', str(t[1]), [], t.lexer.lineno, 0, gramatica)     
            else:
                gramatica = '<cualquiernumero> ::= \"'+str(t[1])+'\"'
                return Nodo('ENTERO', str(t[1]), [], t.lexer.lineno, 0, gramatica)