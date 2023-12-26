from src.ejecucion.environment import Environment
from src.abstract.abstractas import Abstract
from src.manejadorXml import Estructura


class CallFunction(Abstract):
    def __init__(self, row, column, nombre ,listaParametros):
        self.id = nombre
        self.parametros = listaParametros
        super().__init__(row, column)
        
    def accept(self, visitor, environment):
        visitor.visit(self, environment)

    def interpretar(self, environment):
        from src.visitor.tableVisitor import SymbolTableVisitor
        visit = SymbolTableVisitor(environment)
        self.accept(visit, environment)
        # if visit.correct == True:
            #self.accept(visit, environment)
            # print("Ejecutando llamda de una funcion")
            # env = Environment(environment)
            # nombreFuncion = Estructura.nombreActual + "-"+self.id
            # funcion = env.getFuncion(nombreFuncion)
            # funcion.interpretar(env)
            # return self
            

