
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
        