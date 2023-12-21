from src.abstract import Abstract
from abc import abstractmethod
from src.ejecucion.type import Type


class SQLExpression(Abstract):
    def __init__(self, fila, columna, tipo: Type | None = None):
        super().__init__(fila, columna)
        self.tipo = tipo
        self.valor = None

    @abstractmethod
    def accept(self, visitor, environment):
        pass

    @abstractmethod
    def interpretar(self, environment):
        pass


class SQLBinaryExpression(SQLExpression):
    def __init__(self, fila, columna, left: SQLExpression, operator: str, right: SQLExpression,
                 tipo: Type | None = None):
        super().__init__(fila, columna, tipo)
        self.left = left
        self.operator = operator
        self.right = right

    def accept(self, visitor, environment):
        self.left.accept(visitor, environment)
        self.right.accept(visitor, environment)
        visitor.visit(self, environment)

    def interpretar(self, environment):
        from src.visitor.check_expressions_visitor import ExpressionsVisitor
        visitor = ExpressionsVisitor(environment)
        visitor.visit(self, environment)
        if visitor.correct:
            pass
        else:
            return None


class SQLLogicalExpression(SQLBinaryExpression):
    pass


class SQLUnaryExpression(SQLExpression):

    def __init__(self, fila, columna, argument, tipo: Type | None = None):
        super().__init__(fila, columna, tipo)
        self.argument = argument

    def accept(self, visitor, environment):
        if not isinstance(self.argument, (int, str)):
            self.argument.accept(visitor, environment)
        visitor.visit(self, environment)

    def interpretar(self, environment):
        # TODO: Implement
        pass
