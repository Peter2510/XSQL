from src.ejecucion.environment import Environment
from src.expresiones.variable import Variable
from src.manejadorXml import Estructura
from src.visitor.visitor import Visitor


class SymbolTableVisitor(Visitor):
          
    def visitFunctionDeclaration(self, node,environment):
      
        nombre = Estructura.nombreActual + "-" + str(node.id)
        
        if(not environment.existeFuncion(nombre)):
            print(self.correct)
            print("creando nuevo environment")
            environmentFuncion = Environment(environment)
            #validar argumentos y agregarlos a la funcion
            self.visitParamFunction(node,environmentFuncion)
            
            #validar las declaraciones en la funcion
            if self.correct:
                self.visitInstrucciones(node,environmentFuncion)
                if not self.correct:
                    environment.errors = environment.getErrores() + environmentFuncion.getErrores()
                    return None
                else:
                    for variable in environmentFuncion:
                        print(variable.id,variable.value,variable.type)
            else:
                environment.errors = environment.getErrores() + environmentFuncion.getErrores()
                return None
        else:
            print("La funcion ya existe")
            environment.addError("Semantico", node.id ,f"La funcion '{node.id}' ya está definida en la base de datos "+Estructura.nombreActual, node.fila,node.columna)
            return None
            
    def visitParamFunction(self,node,environment):
        if(node.params != None):               
            self.ValidateParamNames(node,environment)
        
    def ValidateParamNames(self,node,environment):
        params = node.params
        seen = set()
        duplicates = set()

        for param in params:
            if param.id in seen:
                duplicates.add(param)
            else:
                seen.add(param.id)

        #si hay duplicados agregarlos al list de errores si no agregarlos a la tabla de simbolos de la funcion
        if duplicates:
            for duplicate in duplicates:
                environment.addError("Semantico", duplicate.id ,f"El id '{duplicate.id}' ya está definido como parámetro", duplicate.fila,duplicate.columna)
                self.correct = False
        else:
            #Agregar parametros como variables
            for param in params:
                v = Variable()
                v.id = param.id
                v.type = param.type
                v.valor = None
                environment.agregarVariable(v)
    
    def visitInstrucciones(self,node,environment):
        instrucciones = node.body
        print("visitando instrucciones")
        for instruccion in instrucciones:
            #entra si son declaraciones de variables, es una lista
            if(isinstance(instruccion,list)):
                for instuc in instruccion:
                    if self.correct:
                        instuc.accept(self,environment)
                    else: 
                        break
            else:
                instruccion.accept(self,environment)
    
    def visitVariableDeclaration(self,node,environment):
        if environment.existeVariable(node.id):
            environment.addError("Semantico", node.id ,f"La variable '{node.id}' ya ha sido definida", node.fila,node.columna)
            self.correct = False
        else:
            v = Variable()
            v.id = node.id
            v.type = node.type
            environment.agregarVariable(v)
           
    def visitAlterFunction(self,node,environment):
        pass
    
    def visitCallFunction(self,node,environment):
        pass
    
    def visitReturn(self,node,environment):
        print("visitando return")
        pass
    
    def visitSet(self,node,environment):
        print("visitando set")
        if(environment.existeVariable(node.id)):
            variable = environment.getVariable(node.id)
            value = node.valor.interpretar(environment)
            if value != None:
               
                if variable.type == value.type:
                    variable.value = value.value
                else:
                    environment.addError("Semantico", node.id ,f"El tipo de dato de la variable no coincide con el valor a asignar", node.fila,node.columna)
                    self.correct = False
            
            else:
                self.correct = False
                       
        else:
             environment.addError("Semantico", node.id ,f"La variable no ha sido declarada", node.fila,node.columna)
             
    def tipoVariableBinaria(self,value,environment):
        pass
                   
                
    def visitPrimitivo(self,node,environment):
        pass
        
    def visitBinaria(self,node,environment):
        ##get value and type    
        pass
    
    def visitRelacionales(self,node,environment):
        ##get value and type
        pass
    
    def visitLogicas(self,node,environment):
        ##get value and type
        pass
    
    def visitRelacional(self,node,environment):
        ##get value and type
        pass
    
    def visitAlterProcedure(self,node,environment):
        pass
    
    def visitCallProcedure(self,node,environment):
        pass
    
    def visitCreateProcedure(self,node,environment):
        pass    
    
    def visitElse(self,node,environment):
        print("visit else")
        pass
    
    def visitElseIf(self,node,environment):
        print("visit elseif")
    
    def visitIf(self,node,environment):
        print("visit if")
        
    
    def visitStmIf(self,node,environment):
        print("visitando ifSTM")
        
    
    def visitElseCase(self,node,environment):
        pass
    
    def visitWhen(self,node,environment):
        pass
    
    def visitStmCase(self,node,environment):
        pass
    
