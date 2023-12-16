from abc import ABC, abstractmethod

class Abstract(ABC):
    
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna
    
    @abstractmethod
    def accept(self, visitor, environment):
        pass

    @abstractmethod
    def interpretar(self, environment):
        pass