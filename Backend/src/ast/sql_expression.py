from src.abstract import Abstract
from abc import abstractmethod
from src.ejecucion.type import Type
from src.expresiones.variable import Variable


class SQLExpression(Abstract):
    def __init__(self, fila, columna, tipo: Type | None = None):
        super().__init__(fila, columna)
        self.tipo = tipo
        self.valor = None
        self.in_paren = False

    def __str__(self):
        return ""

    @abstractmethod
    def accept(self, visitor, environment):
        pass

    @abstractmethod
    def interpretar(self, environment):
        pass


def get_value(exp: SQLExpression, interact: SQLExpression):
    if exp.tipo in [Type.BIT] and interact.tipo in [Type.INT, Type.DECIMAL]:
        return int(exp.valor)

    if exp.tipo in [Type.BIT] and interact.tipo in [Type.TEXT]:
        return str(int(exp.valor))

    if interact.tipo == Type.TEXT:
        return str(exp.valor)

    return exp.valor


class SQLBinaryExpression(SQLExpression):
    def __init__(self, fila, columna, left: SQLExpression, operator: str, right: SQLExpression,
                 tipo: Type | None = None):
        super().__init__(fila, columna, tipo)
        self.left = left
        self.operator = operator
        self.right = right

    def __str__(self):
        op_str = f"{str(self.left)} {self.operator} {str(self.right)}"
        return f"({op_str})" if self.in_paren else op_str

    def accept(self, visitor, environment):
        self.left.accept(visitor, environment)
        self.right.accept(visitor, environment)
        visitor.visit(self, environment)


                
 
    def interpretar(self, environment):
        self.left.interpretar(environment)
        self.right.interpretar(environment)

        if self.left.valor is None or self.right.valor is None:
            return None

        left_value = get_value(self.left, self.right)
        right_value = get_value(self.right, self.left)

        # Special cases
        if self.operator == '/' and right_value == 0:
            environment.addError("Semántico", "0", "0 no puede ser un divisor", self.left.fila, self.left.columna)
            self.valor = 0
        elif self.operator == '+' and self.left.tipo in [Type.BIT] and self.right.tipo in [Type.BIT]:
            self.valor = left_value or right_value
        elif self.operator == '*' and self.left.tipo in [Type.BIT] and self.right.tipo in [Type.BIT]:
            self.valor = left_value and right_value
        elif self.operator in ['*', '/'] and self.left.tipo in [Type.DATETIME, Type.DATE] and self.right.tipo in [
            Type.TEXT]:
            self.valor = left_value + right_value
        elif self.operator in ['*', '/'] and self.right.tipo in [Type.DATETIME, Type.DATE] and self.left.tipo in [
            Type.TEXT]:
            self.valor = left_value + right_value
        elif self.operator == '+':
            self.valor = left_value + right_value
        elif self.operator == '-':
            self.valor = left_value - right_value
        elif self.operator == '*':
            self.valor = left_value * right_value
        elif self.operator == '/':
            self.valor = left_value / right_value
        elif self.operator == '=':
            self.valor = left_value == right_value
        elif self.operator == '!=':
            self.valor = left_value != right_value
        elif self.operator == '>':
            self.valor = left_value > right_value
        elif self.operator == '<':
            self.valor = left_value < right_value
        elif self.operator == '>=':
            self.valor = left_value >= right_value
        elif self.operator == '<=':
            self.valor = left_value <= right_value
        elif self.operator == 'and':
            self.valor = left_value and right_value
        elif self.operator == 'or':
            self.valor = left_value or right_value

        return self.valor


class SQLLogicalExpression(SQLBinaryExpression):
    pass


class SQLUnaryExpression(SQLExpression):

    def __init__(self, fila, columna, argument, tipo: Type | None = None):
        super().__init__(fila, columna, tipo)
        self.argument = argument

    def __str__(self):
        if not isinstance(self.argument, (int, str, float, bool)):
            return str(self.argument)

        return f"({self.argument})" if self.in_paren else str(self.argument)

    def get_tipo(self):
        if not isinstance(self.argument, (int, str, float, bool)):
            return self.argument.tipo

        return self.tipo

    def accept(self, visitor, environment):
        if not isinstance(self.argument, (int, str, float, bool)):
            self.argument.accept(visitor, environment)
        visitor.visit(self, environment)

    def interpretar(self, environment):
        if not isinstance(self.argument, (int, str, float, bool)):
            self.valor = self.argument.interpretar(environment)
        else:
            self.valor = self.argument

        if isinstance(self.valor, Variable):
            self.valor = self.valor.value

        return self.valor
