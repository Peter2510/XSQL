from src.ejecucion.type import Type
from src.expresiones.variable import Variable
from src.abstract.abstractas import Abstract

class Return_(Abstract):
    def __init__(self, row,column, instruction):
        super().__init__(row,column)
        self.instruction = instruction

    def accept(self, visitor, environment):
        visitor.visit(self,environment)
        
    def interpretar(self,environment):
        var = Variable()
        #print("<<<< ESTE ES EL TIPO",type(self.instruction),self.instruction.valor)
        for i in environment:
            print(i.value,i.type,i.id)
        import src.expresiones.binaria as bin 
        
        if isinstance(self.instruction,bin.Binaria):
            
            opDer = self.instruction.opDer
            opDVal = str(opDer.valor)
            opIzq = self.instruction.opIzq
            opIVal = str(opIzq.valor)
            
        
            if opDVal.startswith("@"):
                opDer.tipo = Type.IDDECLARE
            if opIVal.startswith("@"):
                opIzq.tipo = Type.IDDECLARE           
                
            inst = self.instruction.interpretar(environment)
            var.value = inst.value
            var.type = inst.type
            return var
            
        elif isinstance(self.instruction.valor,str) and self.instruction.valor.startswith("@"):
            variable = environment.getVariable(self.instruction.valor)
            var.type = variable.type
            var.value = variable.value
            
            return var
        else:
            inst = self.instruction.interpretar(environment)
            
            var.value = inst.value
            var.type = inst.type
            return var