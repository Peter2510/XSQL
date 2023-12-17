from src.visitor.visitor import Visitor


class SymbolTableVisitor(Visitor):
    functions = {}
    procedures = {}
    
        
    def visitFunctionDeclaration(self, node,environment):
        # Realiza validaciones para cada atributo de FunctionDeclaration
        print("sdf")

    def validate_id(self, id):
        # Realiza validaciones específicas para el atributo 'id'
        print("validando id")
        pass

    def validate_params(self, params):
        # Realiza validaciones específicas para el atributo 'params'
        print("validando params")
        pass

    def validate_type(self, type_):
        print("validando type")
        # Realiza validaciones específicas para el atributo 'type'
        pass

    def validate_body(self, body):
        print("validando body")
        # Realiza validaciones específicas para el atributo 'body'
        pass
    
    def visitAlterFunction(self,node,environment):
        pass
    
    def visitCallFunction(self,node,environment):
        pass
    
    def visitReturn(self,node,environment):
        pass
    
    def visitSet(self,node,environment):
        pass
    
    def visitVariableDeclaration(self,node,environment):
        
        pass
    
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