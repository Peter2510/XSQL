from .visitor import Visitor

class FunctionParamVisitor(Visitor):

    def __init__(self, environment):
        super().__init__(environment)

    def visitFunctionParam(self, node, environment):
        print("ENTRANDO AL VISITOR DEL PARAMETRO")
        
    
    