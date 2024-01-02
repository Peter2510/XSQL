from src.ejecucion.environment import Environment
from src.abstract.abstractas import Abstract
from src.manejadorXml import Estructura


class CallFunction(Abstract):
    def __init__(self, row, column, nombre ,listaParametros):
        self.id = nombre
        self.parametros = listaParametros
        self.tipo = None
        super().__init__(row, column)

    def __str__(self):
        return f"{self.id}()"
    def accept(self, visitor, environment):
        from src.visitor import ValidateColumnVisitor
        from src.ast import TableColumn
        from src.expresiones.primitivos import Primitivo
        if isinstance(visitor, ValidateColumnVisitor):
            for column in self.parametros:
                if isinstance(column, Primitivo) and isinstance(column.valor, TableColumn):
                    column.valor.accept(visitor, environment)
        return visitor.visit(self, environment)

    def interpretar(self, environment):
        from src.visitor.tableVisitor import SymbolTableVisitor
        visit = SymbolTableVisitor(environment)
        return self.accept(visit, environment)
        # if visit.correct == True:
            #self.accept(visit, environment)
            # print("Ejecutando llamda de una funcion")
            # env = Environment(environment)
            # nombreFuncion = Estructura.nombreActual + "-"+self.id
            # funcion = env.getFuncion(nombreFuncion)
            # funcion.interpretar(env)
            # return self
            

