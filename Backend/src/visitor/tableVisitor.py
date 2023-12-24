from src.ejecucion.type import Type
from src.instrucciones.funcion.string_ import String_
from src.instrucciones.funcion.funcion import Funcion
from src.ejecucion.environment import Environment
from src.expresiones.variable import Variable
from src.manejadorXml import Estructura
from src.visitor.visitor import Visitor


class SymbolTableVisitor(Visitor):
          
    def visitFunctionDeclaration(self, node,environment):
      
        nombre = Estructura.nombreActual + "-" + str(node.id)
        self.tipo = node.type
        
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
                    funcion = Funcion(node.id,node.type,node.params,node.body)
                    environment.agregarFuncion(nombre,funcion)
                    #environment.getFuncion(nombre).interpretar(environmentFuncion)
                        
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
        print("visitando alter function")
        nombre = Estructura.nombreActual + "-" + str(node.id)
        if environment.existeFuncion(nombre):
            
            del environment.funciones[nombre]
            self.visitFunctionDeclaration(node,environment)
            
        
        else:
            environment.addError("Semantico", node.id ,f"La funcion '{node.id}' no existe en la base de datos "+Estructura.nombreActual, node.fila,node.columna)
        
    
    def visitCallFunction(self,node,environment):
        pass
    
    def visitReturn(self,node,environment):
        
        valorRetorno = node.instruction.interpretar(environment)
        
        if valorRetorno != None:
            
            #validar si es de tipo string
            if isinstance(self.tipo, String_):
                
                tamanio = self.tipo.size.interpretar(environment)
                
                if valorRetorno.type == Type.TEXT:
                    
                    if self.tipo.type == Type.NVARCHAR:
                        
                        if not (len(valorRetorno.value) <= tamanio.value):
                            environment.addError("Semantico", valorRetorno.value ,f"No es posible retornar una cadena de longitud {len(valorRetorno.value)}, el tamaño debe ser minino 0 y maximo {tamanio.value}", node.fila,node.columna)
                            self.correct = False                      
                    
                    else:

                        if not (len(valorRetorno.value) <= tamanio.value and len(valorRetorno.value) >= 1) :
                            environment.addError("Semantico", valorRetorno.value ,f"No es posible retornar una cadena de longitud {len(valorRetorno.value)}, el tamaño debe ser minino 1 y maximo {tamanio.value}", node.fila,node.columna)
                            
                            self.correct = False
                                                                               
                else: 
                    environment.addError("Semantico", valorRetorno.value ,f"El tipo de dato retornado debe ser de tipo {self.tipo.type.name}", node.fila,node.columna)
                    self.correct = False
    
            #validar si es de tipo bit
            elif self.tipo == Type.BIT:
                
                if not(valorRetorno.value == 0 or valorRetorno.value == 1):
                    environment.addError("Semantico", valorRetorno.value ,f"No es posible retornar un {valorRetorno.type.name}, el tipo de dato de la funcion es BIT", node.fila,node.columna)
                    self.correct = False            
                        
            else:

                if not valorRetorno.type == self.tipo:
                    environment.addError("Semantico", valorRetorno.value ,f"El tipo de retorno no coincide con el tipo de la funcion", node.fila,node.columna)
                    self.correct = False
            
        else:
            environment.addError("Semantico", "" ,f"Error en el valor de retorno", node.fila,node.columna)    
                    
    def visitSet(self,node,environment):
        print("visitando set")
        
        if(environment.existeVariable(node.id)):
            variable = environment.getVariable(node.id)
            value = node.valor.interpretar(environment)
            if value != None:
                
                if isinstance(variable.type,String_):
                    tamanio = variable.type.size.interpretar(environment)
                    if value.type == Type.TEXT:
                    
                        if variable.type.type == Type.NVARCHAR:
                            if len(value.value) <= tamanio.value:
                                variable.value = value.value
                            else:
                                environment.addError("Semantico", value.value ,f"No es posible asignar a {node.id} una cadena de longitud {len(value.value)}, la variable es de tipo {variable.type.type.name}({tamanio.value}), el tamaño debe ser minino 0 y maximo {tamanio.value}", node.fila,node.columna)
                                self.correct = False
                        else:
                        
                            if len(value.value) <= tamanio.value and len(value.value) > 0:
                                variable.value = value.value
                            else:
                                environment.addError("Semantico", value.value ,f"No es posible asignar a {node.id} una cadena de longitud {len(value.value)}, la variable es de tipo {variable.type.type.name}({tamanio.value}), el tamaño debe ser minino 1 y maximo {tamanio.value}", node.fila,node.columna)
                                self.correct = False    
                                                       
                    else: 
                        environment.addError("Semantico", value.value ,f"No es posible asignar a {node.id} un {value.type.name}, la variable es de tipo {variable.type.type.name}({tamanio.value}), el tamaño debe ser minino 0 y maximo {tamanio.value}", node.fila,node.columna)                        
                        self.correct = False
                    
                else:
                    
                    #validar las asignaciones de tipo bit
                    
                    if variable.type == Type.BIT:
                    
                        if value.type == Type.INT:
                            if value.value == 0 or value.value == 1:
                                variable.value = value.value
                            else:
                                environment.addError("Semantico", value.value ,f"No es posible asignar a {node.id} un {value.type.name}, la variable es de tipo {variable.type.name}", node.fila,node.columna)
                                self.correct = False
                                                       
                            
                        elif value.type == Type.BIT:
                            variable.value = value.value
                    
                        else:
                            environment.addError("Semantico", value.value ,f"No es posible asignar a {node.id} un {value.type.name}, la variable es de tipo {variable.type.name}", node.fila,node.columna)
                            self.correct = False                            
                    
                    else: 
                        
                        if variable.type == value.type:
                            variable.value = value.value
                        else:
                            environment.addError("Semantico", value.value ,f"No es posible asignar a {node.id} un {value.type.name}, la variable es de tipo {variable.type.name}", node.fila,node.columna)
                            self.correct = False
            
            else:
                self.correct = False               
        else:
             environment.addError("Semantico", node.id ,f"La variable no ha sido declarada", node.fila,node.columna)
             self.correct = False               
                 
    def visitAlterProcedure(self,node,environment):
        pass
    
    def visitCallProcedure(self,node,environment):
        pass
    
    def visitCreateProcedure(self,node,environment):
        pass    
    
    def visitElse(self,node,environment):
        print("visitando esle")
        env = Environment(environment)
               
        for inst in node.instructions:
            if isinstance(inst,list):
                for instruccion in inst:
                    if self.correct:
                        instruccion.accept(self,env)
                    else: 
                         self.correct = False
                         break
            else:
                inst.accept(self,env)        
        environment.errors = environment.getErrores() + env.getErrores()            
        
    
    def visitElseIf(self,node,environment):
        condicion = node.condition.interpretar(environment)
        env = Environment(environment)
        if condicion != None:
            
            if condicion.type == Type.BIT:
                for inst in node.instructions:
                    if isinstance(inst,list):
                        for instruccion in inst:
                            if self.correct:
                                instruccion.accept(self,env)
                            else: 
                                self.correct = False
                                break
                    else:
                        inst.accept(self,env)
                
                environment.errors = environment.getErrores() + env.getErrores()
            else: 
                environment.addError("Semantico", "" ,f"La condicion de la sentencia ElseIf debe ser de tipo BIT", node.fila,node.columna)
                self.correct = False
                
        else: 
            environment.addError("Semantico", "" ,f"Error en la condicion de la sentencia ElseIf", node.fila,node.columna)
            self.correct = False
    
    def visitIf(self,node,environment):
        
        condicion = node.condition.interpretar(environment)
        env = Environment(environment)
        if condicion != None:
            
            if condicion.type == Type.BIT:
                for inst in node.instructions:
                    if isinstance(inst,list):
                        for instruccion in inst:
                            if self.correct:
                                instruccion.accept(self,env)
                            else: 
                                self.correct = False
                                break
                    else:
                        inst.accept(self,env)
                
                environment.errors = environment.getErrores() + env.getErrores()
            else: 
                environment.addError("Semantico", "" ,f"La condicion de la sentencia if debe ser de tipo BIT", node.fila,node.columna)
                self.correct = False
                
        else: 
            environment.addError("Semantico", "" ,f"Error en la condicion de la sentencia if", node.fila,node.columna)
            self.correct = False
        
    
    def visitStmIf(self,node,environment):
        print("visitando ifSTM")
        
    
    def visitElseCase(self,node,environment):
        print("visitando esle")
        env = Environment(environment)
               
        for inst in node.instructions:
            if isinstance(inst,list):
                for instruccion in inst:
                    if self.correct:
                        instruccion.accept(self,env)
                    else: 
                         self.correct = False
                         break
            else:
                inst.accept(self,env)        
        environment.errors = environment.getErrores() + env.getErrores()            
    
    def visitWhen(self,node,environment):
        condicion = node.condition.interpretar(environment)
        env = Environment(environment)
        if condicion != None:
            
            if condicion.type == Type.BIT:
                for inst in node.instructions:
                    if isinstance(inst,list):
                        for instruccion in inst:
                            if self.correct:
                                instruccion.accept(self,env)
                            else: 
                                self.correct = False
                                break
                    else:
                        inst.accept(self,env)
                
                environment.errors = environment.getErrores() + env.getErrores()
            else: 
                environment.addError("Semantico", "" ,f"La condicion de la sentencia when debe ser de tipo BIT", node.fila,node.columna)
                self.correct = False
                
        else: 
            environment.addError("Semantico", "" ,f"Error en la condicion de la sentencia when", node.fila,node.columna)
            self.correct = False
    
    def visitStmCase(self,node,environment):
        pass
    
