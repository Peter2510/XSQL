from src.expresiones.binaria import Binaria
from src.instrucciones.funcion.call_function import CallFunction
from src.instrucciones.funcion.return_ import Return_
from src.ejecucion.type import Type
from src.instrucciones.funcion.string_ import String_
from src.instrucciones.funcion.funcion import Funcion
from src.ejecucion.environment import Environment
from src.expresiones.variable import Variable
from src.manejadorXml import Estructura
from src.visitor.visitor import Visitor


class SymbolTableVisitor(Visitor):
    
    def __init__(self, valor=None):
        self.tipo = valor
        self.correct = True
             
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
                        
            else:
                environment.errors = environment.getErrores() + environmentFuncion.getErrores()
                return None
        else:
            self.correct = False
            environment.addError("Semantico", node.id ,f"La funcion '{node.id}' ya está definida en la base de datos "+Estructura.nombreActual, node.fila,node.columna)
            return None
            
    def visitParamFunction(self,node,environment):
        if(len(node.params)>0):               
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
                
                if v.type == Type.INT:
                    v.value = 0
                elif v.type == Type.DECIMAL:
                    v.value = 0.0
                elif isinstance(v.type,String_):    
                    v.value = ""
                elif v.type == Type.TEXT:
                    v.value = ""
                elif v.type == Type.BIT:
                    v.value = False
                elif v.type == Type.DATE:
                    v.value = "1999-01-01"
                elif v.type == Type.DATETIME:
                    v.value = "1999-01-01 00:00:00"
                elif v.type == Type.NULL:
                    v.value = ""
                            
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
            if node.type == Type.INT:
                v.value = 0        
            elif node.type == Type.DECIMAL:
                v.value = 0.0
            elif isinstance(node.type,String_):
                v.value = ""
            elif node.type == Type.TEXT:
                v.value = ""
            elif node.type == Type.BIT:
                v.value = False
            elif node.type == Type.DATE:
                v.value = "1999-01-01"
            elif node.type == Type.DATETIME:
                v.value = "1999-01-01 00:00:00"
            elif node.type == Type.NULL:
                v.value = ""
            
            environment.agregarVariable(v)
           
    def visitAlterFunction(self,node,environment):
        print("visitando alter function")
        nombre = Estructura.nombreActual + "-" + str(node.id)
        if environment.existeFuncion(nombre):
            
            del environment.funciones[nombre]
            self.visitFunctionDeclaration(node,environment)
            
        
        else:
            environment.addError("Semantico", node.id ,f"La función '{node.id}' no existe en la base de datos: "+Estructura.nombreActual, node.fila,node.columna)
            self.correct = False
        
    
    def visitCallFunction(self,node,environment):
        print("visitando call function")
        nombre = Estructura.nombreActual + "-" + str(node.id)
        #validar si existe la funcion
        if environment.existeFuncion(nombre):
            print("Existe la funcion")
            funcion = environment.getFuncion(nombre)
            
            if len(funcion.parametros) > 0:
            
                
            
                if len(node.parametros) == len(funcion.parametros):

                    print("tiene la misma cantidad de parametros")
                    
                    env = Environment()     

                    #ejecutar parametros   
                    #comparar el tipo, si son iguales agregar la variable
                    #luego ejeuctar las instrucciones
                    for i in range(len(node.parametros)):

                        parametro = funcion.parametros[i] #definicion
                        argumento = node.parametros[i].interpretar(env)#llamada
                        print("EN PARAEMTROS",parametro,argumento)

                        if parametro != None and argumento != None:   

                            #validar si es de tipo string
                            if isinstance(parametro.type, String_):
                            
                                tamanio = parametro.type.size.interpretar(env)
                                print("tipo de lo recibido",parametro.type.type.name)
                                print("argumento: ",argumento.value,argumento.type)
                                if argumento.type == Type.TEXT:
                                
                                    if parametro.type.type.name == Type.NVARCHAR:
                                    
                                        if not (len(argumento.value) <= tamanio.value):
                                             env.addError("Semantico", argumento.value ,f"La longitud del argumento es mayor a la permitida en la funcion, el tamaño debe ser minino 0 y maximo {tamanio.value}", node.fila,node.columna)
                                             self.correct = False                      
                                        else:

                                             variable = env.getVariable(node.id)
                                             variable.value = argumento.value
                                             #for variable in env:
                                             print("new variable",variable)

                                    else:

                                        if not (len(argumento.value) <= tamanio.value and len(argumento.value) >= 1):
                                            env.addError("Semantico", argumento.value ,f"La longitud del argumento es mayor a la permitida en la funcion, el tamaño debe ser minino 1 y maximo {tamanio.value}", node.fila,node.columna)                        
                                            self.correct = False

                                        else:

                                             #agregar la variable al env ya con valor
                                             
                                             #for variable in env:
                                             print(variable)


                                else: 
                                     env.addError("Semantico", argumento.value ,f"Se esperaba un parametro de tipo TEXT, {argumento.value} no cumple con la condicion", node.fila,node.columna)
                                     self.correct = False
                                     environment.errors = environment.getErrores() + env.getErrores()


                            elif argumento.type == Type.BIT:
                            
                                 if not(argumento.value == 0 or argumento.value == 1):
                                     env.addError("Semantico", argumento.value ,f"{argumento.type.name}, el argumento debe ser de tipo BIT", node.fila,node.columna)
                                     self.correct = False  
                                     environment.errors = environment.getErrores() + env.getErrores()

                                 else:
                                        variable = env.getVariable(node.id)
                                        variable.value = argumento.value
                                        #for variable in env:
                                        print(variable)

                            else:
                                 print("Argumento recibido",argumento.value,argumento.type,argumento.id)
                                 print("Parametro recibido",parametro.type)
                                 
                                 #if not argumento.type == parametro:
                                 #    env.addError("Semantico", argumento.value ,f"Se esperaba un parametro de tipo {parametro.name} y se hallo un tipo {argumento.type.name}", node.fila,node.columna)
                                 #    self.correct = False
                                 #else:
                                 #           variable = env.getVariable(node.id)
                                 #           variable.value = argumento.value
                                 #           #for variable in env:
                                 #            print(variable)

                        else:
                             self.correct = False
                             environment.errors = environment.getErrores() + env.getErrores()
                             break
                         
                    #ejecutar instrucciones
                else:
                    environment.addError("Semantico", node.id ,f"La invocacion de la función '{node.id}' no tiene la misma cantidad de parametros que la función almacenada", node.fila,node.columna)
                    self.correct = False
               
            else:
                env1 = Environment()
                valorEjecucion = funcion.interpretar(env1)
                #print("desde visitCallFunction",valorEjecucion.value,valorEjecucion.type)
                return valorEjecucion
                
                    
        else:
            environment.addError("Semantico", node.id ,f"La funcion '{node.id}' no existe en la base de datos "+Estructura.nombreActual, node.fila,node.columna)
            self.correct = False
    
    def visitReturn(self,node,environment):
        
        valorRetorno = node.instruction.interpretar(environment)
        #print("valor retorno",valorRetorno,type(valorRetorno.type),valorRetorno.value,valorRetorno.id)
        
        if valorRetorno != None:
            
            #validar si es de tipo string
            if isinstance(self.tipo, String_):
                
                tamanio = self.tipo.size.interpretar(environment)
                
                if isinstance(valorRetorno.type,String_):
                    
                    if self.tipo.type == Type.NVARCHAR:
                        
                        if not (len(valorRetorno.value) <= tamanio.value):
                            environment.addError("Semantico", valorRetorno.value ,f"No es posible retornar una cadena de longitud {len(valorRetorno.value)}, el tamaño debe ser minino 1 y maximo {tamanio.value}", node.fila,node.columna)
                            self.correct = False                      
                        else:
                            return valorRetorno
                    
                    else:

                        if not (len(valorRetorno.value) <= tamanio.value and len(valorRetorno.value) >= 1) :
                            environment.addError("Semantico", valorRetorno.value ,f"No es posible retornar una cadena de longitud {len(valorRetorno.value)}, el tamaño debe ser minino 1 y maximo {tamanio.value}", node.fila,node.columna)
                            self.correct = False
                        else: 
                            return valorRetorno
                                                                               
                else: 
                    environment.addError("Semantico", valorRetorno.value ,f"El tipo de dato retornado debe ser de tipo {self.tipo.type.name}", node.fila,node.columna)
                    self.correct = False
    
            #validar si es de tipo bit
            elif self.tipo == Type.BIT:
                
                if not(valorRetorno.value == 0 or valorRetorno.value == 1):
                    environment.addError("Semantico", valorRetorno.value ,f"No es posible retornar un {valorRetorno.type.name}, el tipo de dato de la funcion es BIT", node.fila,node.columna)
                    self.correct = False 
                else:
                    return valorRetorno           
                        
            else:

                if not valorRetorno.type == self.tipo:
                    environment.addError("Semantico", valorRetorno.value ,f"No es posible retornar un {valorRetorno.type.name}, el tipo de dato de la funcion es {self.tipo.name}", node.fila,node.columna)
                    self.correct = False
                else: 
                    return valorRetorno
            
            
        else:
            environment.addError("Semantico", "" ,f"Error en el valor de retorno", node.fila,node.columna)    
            self.correct = False
                    
    def visitSet(self,node,environment):
        
        if(environment.existeVariable(node.id)):
            
            variable = environment.getVariable(node.id)
            
            #print(variable.toString(),"jkajka")
            
            if isinstance(node.valor,CallFunction):
                
                valor = node.valor.interpretar(environment)
                
                #print("Esto retorna desde la llamada",valor)
                
                if valor != None:

                    if isinstance(variable.type,String_):
                        #print("SI ES DE TIPO STRING_")
                        tamanio = variable.type.size.interpretar(environment)
                        
                        if variable.type.type == Type.NVARCHAR:
                                if len(valor.value) <= tamanio.value:
                                    variable.value = valor.value
                                    #variable.type = Type.TEXT
                                
                                else:
                                    environment.addError("Semantico", valor.value ,f"No es posible asignar a {node.id} una cadena de longitud {len(valor.value)}, la variable es de tipo {variable.type.type.name}({tamanio.value}), el tamaño debe ser minino 0 y maximo {tamanio.value}", node.fila,node.columna)
                                    self.correct = False
                        else:
                        
                                if len(valor.value) <= tamanio.value and len(valor.value) > 0:
                                    variable.value = valor.value
                                    #variable.type = Type.TEXT
                                else:
                                    environment.addError("Semantico", valor.value ,f"No es posible asignar a {node.id} una cadena de longitud {len(valor.value)}, la variable es de tipo {variable.type.type.name}({tamanio.value}), el tamaño debe ser minino 1 y maximo {tamanio.value}", node.fila,node.columna)
                                    self.correct = False    
                                                       
                        
                    
                    else:
                        
                        #validar las asignaciones de tipo bit
                    
                        if variable.type == Type.BIT:
                    
                            if valor.type == Type.INT:
                                if valor.value == 0 or valor.value == 1:
                                    variable.value = valor.value
                                else:
                                    environment.addError("Semantico", valor.value ,f"No es posible asignar a {node.id} un {valor.type.name}, la variable es de tipo {variable.type.name}", node.fila,node.columna)
                                    self.correct = False
                                             
                            elif valor.type == Type.BIT:
                                variable.value = valor.value
                    
                            else:
                                environment.addError("Semantico", valor.value ,f"No es posible asignar a {node.id} un {valor.type.name}, la variable es de tipo {variable.type.name}", node.fila,node.columna)
                                self.correct = False                            
                    
                        else: 
                        
                            if variable.type == valor.type:
                                variable.value = valor.value
                            else:
                                environment.addError("Semantico", valor.value ,f"No es posible asignar a {node.id} un {valor.type.name}, la variable es de tipo {variable.type.name}", node.fila,node.columna)
                                self.correct = False
            
                else:
                    self.correct = False  
            
            else:
                
                print("Entra")
                value = node.valor.interpretar(environment)    
                print("sale",value)
            
                if value != None:

                    if isinstance(variable.type,String_):
                        
                        tamanio = variable.type.size.interpretar(environment)
                        if value.type == Type.TEXT:
                        
                            if variable.type.type == Type.NVARCHAR:
                                if len(value.value) <= tamanio.value:
                                    variable.value = value.value
                                    #variable.type = Type.TEXT
                                else:
                                    environment.addError("Semantico", value.value ,f"No es posible asignar a {node.id} una cadena de longitud {len(value.value)}, la variable es de tipo {variable.type.type.name}({tamanio.value}), el tamaño debe ser minino 0 y maximo {tamanio.value}", node.fila,node.columna)
                                    self.correct = False
                            else:
                            
                                if len(value.value) <= tamanio.value and len(value.value) > 0:
                                    variable.value = value.value
                                    #variable.type = Type.TEXT
                                else:
                                    environment.addError("Semantico", value.value ,f"No es posible asignar a {node.id} una cadena de longitud {len(value.value)}, la variable es de tipo {variable.type.type.name}({tamanio.value}), el tamaño debe ser minino 1 y maximo {tamanio.value}", node.fila,node.columna)
                                    self.correct = False    

                        else: 
                            environment.addError("Semantico", value.value ,f"No es posible asignar a {node.id} un {value.type.name}, la variable es de tipo {variable.type.type.name}({tamanio.value})", node.fila,node.columna)                        
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
    
