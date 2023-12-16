from .visitor import Visitor

class FunctionDeclarationsVisitor(Visitor):

    def __init__(self, environment):
        super().__init__(environment)

    def visitFunctionDeclaration(self, node, environment):
        print("HACER COMPROBACIONES CON FUNCIONES DECLARACIONES")
        
    def visitFunctionParam(self, node, environment):
        print("ENTRANDO AL VISITOR DEL PARAMETRO")
        
    
    