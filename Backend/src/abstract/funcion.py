from abc import ABC, abstractmethod

class Funcion(ABC):
    
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna
    
    @abstractmethod
    def interpretar(self, environment):
        pass