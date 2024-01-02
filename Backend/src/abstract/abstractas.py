from abc import ABC, abstractmethod

class Abstract(ABC):
    
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna
        # node dot
        self.nd = None

    def __str__(self):
        return ""
    @abstractmethod
    def accept(self, visitor, environment):
        pass

    @abstractmethod
    def interpretar(self, environment):
        pass
