from src.ejecucion.error import T_error

class TablaSimbolos(list):

    def __init__(self, padre=None):
        super().__init__()
        self.errors = []
        if padre is not None:
            for variable in padre:
                self.append(variable)
   
    def addError(self,tipo,token,descripcion,fila,columna):
        self.errors.append(T_error(tipo,token,descripcion,fila,columna))
               
    def setErrores(self, errores):
        self.errors = errores
        
    def getErrores(self):
        return self.errors
       
    def _add(self, variable):
        self.append(variable)

    def getById(self, id):
        for variable in self:
            if variable.getId() == id:
                return variable
        return None

    def contains(self, id):
        for variable in self:
            if variable.getId() == id:
                return True
        return False
        
    