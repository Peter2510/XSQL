from src.instrucciones.funcion.funcion import Simbolo
from src.manejadorXml import Estructura
from src.instrucciones.funcion.return_ import Return_
from src.visitor.visitor import Visitor
from datetime import datetime


class SymbolTableVisitor(Visitor):
   
        
    def visitFunctionDeclaration(self, node,environment):
        
        nombre = Estructura.nombreActual+"-"+node.id
        self.nombreFuncion = nombre
        if(not environment.existeFunction(nombre)):
            #Agregar la funcion Basededatos-NombreFuncion
            environment.agregarFunction(nombre,environment)
            #validar argumentos y agregarlos a la funcion
            self.visitParamFunction(node,environment,nombre)
            #validar las declaraciones en la funcion
            self.visitInstrucciones(node.body,environment,nombre)
        else:
            environment.addError("Semantico", node.id ,f"La funcion '{node.id}' ya está definida en la base de datos "+Estructura.nombreActual, node.fila,node.columna)
            
    def visitParamFunction(self,node,environment,nombre):
        if(node.params != None):               
            self.ValidateParamNames(node.params,environment,nombre)
        
    def ValidateParamNames(self,params,environment,nombre):
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
        else:
            #Agregar parametros como variables
            for param in params:
                if(environment.existeVariable(nombre,param.id)):
                    environment.addError("Semantico", param.id ,f"El id '{param.id}' ya está definido como variable", param.fila,param.columna)
                else:
                    environment.agregarVariable(nombre,param.id,Simbolo(param.type,None))
            #print(len(environment.funciones[0].tablaSimbolos.variables),"valida esto---------")        
            #print("ObtenerVariable",environment.obtenerVariable(nombre,"@productids").valor)
    
    def visitInstrucciones(self,instrucciones,environment,nombre):
        print("visitando instrucciones")
        for instruccion in instrucciones:
            for instuc in instruccion:
                instuc.accept(self,environment)
            
    def visitPrimitivo(self,node,environment):
        return node            
    
    def visitVariableDeclaration(self,node,environment):
        print(len(environment.funciones))
        pass
   
    def visitAlterFunction(self,node,environment):
        pass
    
    def visitCallFunction(self,node,environment):
        pass
    
    def visitReturn(self,node,environment):
        print("visitando return")
        pass
    
    def visitSet(self,node,environment):
        ##print("Nombre valira",node.id,"Nombre funcion",self.nameFunction)
        #visit value and apply method accept
        if(environment.existeVariable(self.nombreFuncion,node.id)):
            #validate that the value is the same type of the variable
             variable = environment.obtenerVariable(self.nombreFuncion,node.id)
             if(variable.tipo == node.value.tipo):
                 variable.valor = node.value.valor
                 print("se asigno el valor a la variable")
             else:
                environment.addError("Semantico", node.id ,f"El tipo de dato no es el mismo que el de la variable", node.fila,node.columna)
        else:
             environment.addError("Semantico", node.id ,f"La variable no existe", node.fila,node.columna)
        print("ObtenerVariable",environment.obtenerVariable(self.nombreFuncion,"@productid").valor)
    
    def visitAlterProcedure(self,node,environment):
        pass
    
    def visitCallProcedure(self,node,environment):
        pass
    
    def visitCreateProcedure(self,node,environment):
        pass    
    
    def visitElse(self,node,environment):
        pass
    
    def visitElseIf(self,node,environment):
        pass
    
    def visitIf(self,node,environment):
        pass
    
    def visitStmIf(self,node,environment):
        pass
    
    def visitElseCase(self,node,environment):
        pass
    
    def visitWhen(self,node,environment):
        pass
    
    def visitStmCase(self,node,environment):
        pass
    
