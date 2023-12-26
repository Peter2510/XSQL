from src.abstract import Abstract
from src.ejecucion.type import Type


class Concatenar(Abstract):
    def __init__(self, fila, columna, expr_lst):
        super().__init__(fila, columna)
        self.expr_lst = expr_lst
        self.tipo = Type.TEXT

    def __str__(self):
        return "Concatena"

    def accept(self, visitor, environment):
        for expr in self.expr_lst:
            expr.accept(visitor, environment)
        visitor.visit(self, environment)

    def interpretar(self, environment):
        result = ""
        for expr in self.expr_lst:
            result = f"{result}{expr.interpretar(environment)}"

        return result