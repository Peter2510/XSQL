from abc import ABC, abstractmethod
from src.ast.symTable import SymTable
from src.visitor.visitor import Visitor

class Node(ABC):
    
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna
    
    @abstractmethod
    def accept(self, visitor:Visitor, ambit:SymTable):
        pass

class Program(Node):

    def __init__(self, fila, columna, body):
        super().__init__(fila, columna)
        self.body = body
        self.table = SymTable('global')
        

    def accept(self, visitor, ambit):
        visitor.setAmbit(self.table)
        for child in self.body:
            child.accept(visitor, self.table)
        visitor.visit(self)

    
class VariableDeclarator(Node):
    def __init__(self, fila,columna, id, init=None):
        super().__init__(fila,columna)
        self.id = id
        self.init = init
        self.type = None
        self.value = None
        self.isParam = False

    def setParam(self):
        self.isParam = True

    def accept(self, visitor, ambit=None):
        if ambit is not None:
            visitor.setAmbit(ambit)
        if self.init is not None:
            self.init.accept(visitor, ambit)
        self.id.accept(visitor, ambit)
        visitor.visit(self)
        
class Expr(Node):
    def __init__(self, fila,columna, type_ = None):
        super().__init__(fila,columna)
        self.type = type_
        self.value = None

    def accept(self, visitor: Visitor, ambit: SymTable = None):
        pass
        
class BinaryExpression(Expr):
    def __init__(self, fila,columna, type_ = None, left: Expr = None, operator: str = '', right: Expr = None):
        super().__init__(fila,columna, type_)
        self.left = left
        self.operator = operator
        self.right = right

    def accept(self, visitor: Visitor, ambit: SymTable = None):
        if ambit is not None:
            visitor.setAmbit(ambit)
        self.left.accept(visitor, ambit)
        self.right.accept(visitor, ambit)
        visitor.visit(self)
        
class LogicalExpression(BinaryExpression):
    pass

class Assignment(Node):
    def __init__(self, fila,columna, id, expression):
        super().__init__(fila,columna)
        self.id = id
        self.expression = expression

    def accept(self, visitor: Visitor, ambit = None):
        if ambit is not None:
            visitor.setAmbit(ambit)
        self.id.accept(visitor, ambit)
        self.expression.accept(visitor, ambit)
        visitor.visit(self)
        
class CallFunction(Node):
    def __init__(self, fila,columna, callee, args):
        super().__init__(fila,columna)
        self.callee = callee
        self.args = args
        self.returnedValue = None

    def accept(self, visitor, ambit = None):
        if ambit is not None:
            visitor.setAmbit(ambit)
        for expr in self.args:
            expr.accept(visitor, ambit)
        visitor.visit(self)

    def get_table_name(self) -> str:
        func_types = ','.join(str(expr.type) if expr.type is not None else 'null' for expr in self.args)
        return f'{self.callee}({func_types})'
    
class FunctionParam(Node):
    def __init__(self, fila,columna, type_, id_):
        super().__init__(fila,columna)
        self.type = type_
        self.id = id_

    def accept(self, visitor, ambit = None):
        if ambit is not None:
            visitor.setAmbit(ambit)
        self.id.accept(visitor, ambit)
        visitor.visit(self)
        
class ReturnStmt(Node):
    def __init__(self, fila,columna, argument=None):
        super().__init__(fila,columna)
        self.argument = argument

    def accept(self, visitor, ambit = None):
        if ambit is not None:
            visitor.setAmbit(ambit)
        if self.argument is not None:
            self.argument.accept(visitor, ambit)
        visitor.visit(self)

class FunctionDeclaration(Node):
    def __init__(self, fila, columna , id, params, type_, body):
        super().__init__(fila,columna)
        self.id = id
        self.params = params
        self.type = type_
        self.body = body
        self.name_for_table = self.get_name_for_table()
        self.table = SymTable(f"funcion {id}")
        self.table.returned_type = self.type

    def accept(self, visitor, ambit = None):
        visitor.set_ambit(self.table)
        if isinstance(visitor, SymTableVisitor):
            visitor.visit(self)
        else:
            for child in self.body:
                child.accept(visitor, self.table)
            for param in self.params:
                param.accept(visitor, self.table)
            visitor.visit(self)

    def get_name_for_table(self) -> str:
        func_types = ','.join(str(param.type) for param in self.params)
        return f"{self.id}({func_types})"
    
