from src.ejecucion.type import Type
from src.expresiones.variable import Variable
from ..abstract.expresion import Expression

class Primitivo(Expression):
    def __init__(self, fila, columna, valor, tipo):
        self.valor = valor
        self.tipo = tipo
        super().__init__(fila, columna)


    def generar_3d(self, tabla, controlador):
        return self

    def get_temp(self):
        return self.valor

    def accept(self, visitor, environment):
        visitor.visit(self, environment)
        

    def interpretar(self, environment):
        variable = Variable()
        
        val = str(self.valor)
        if(val.startswith("@")):
            self.tipo = Type.IDDECLARE
            
        
        if self.tipo == Type.INT:
            variable.type = Type.INT
            variable.value = int(self.valor)
            return variable
        elif self.tipo == Type.DECIMAL:
            variable.type = Type.DECIMAL
            variable.value = float(self.valor)
            return variable
        elif self.tipo == Type.TEXT:
            variable.type = Type.TEXT
            variable.value = str(self.valor)
            return variable
        elif self.tipo == Type.BIT:
            variable.type = Type.BIT
            variable.value = bool(self.valor)
            return variable
        elif self.tipo == Type.DATE:
            variable.type = Type.DATE
            variable.value = self.valor
            return variable
        elif self.tipo == Type.DATETIME:
            variable.type = Type.DATETIME
            variable.value = self.valor
            return variable
        elif self.tipo == Type.NULL:
            variable.type = Type.NULL
            variable.value = None
            return variable
        elif self.tipo == Type.ID:
            #buscar si existe la tabla
            pass
        elif self.tipo == Type.IDDECLARE:
            tmp = environment.existeVariable(str(self.valor))
            if tmp == True:
                var = environment.getVariable(str(self.valor))
                variable.id = var.id
                self.tipo = var.type
                variable.type = var.type
                variable.value = var.value
                return variable
            else:
                print("La variable " + str(self.valor) + " no está definida")
                environment.addError("Semántico", str(self.valor), "La variable no está definida", self.fila, self.columna)
                return None
        
         