from src.manejadorXml import Estructura
from src.instrucciones.funcion.return_ import Return_
from src.visitor.visitor import Visitor


class UsarVisitor(Visitor):
    
   def visitUsar(self,node,environment):
        nombre = node.nombre
        Estructura.nombreActual = nombre
        pass