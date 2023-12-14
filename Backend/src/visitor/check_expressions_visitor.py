from enum import Enum
from .visitor import Visitor
from src.ejecucion.type import Type


COMBINATIONS = [
    f'{Type.INT.name}-{Type.INT.name}',
    f'{Type.INT.name}-{Type.DECIMAL.name}',
    f'{Type.INT.name}-{Type.TEXT.name}',
    f'{Type.DECIMAL.name}-{Type.DECIMAL.name}',
    f'{Type.DECIMAL.name}-{Type.TEXT.name}',
    f'{Type.TEXT.name}-{Type.TEXT.name}',
]

ADDITION_CAST = [
    Type.INT.name,
    Type.DECIMAL.name,
    Type.TEXT.name,
    Type.DECIMAL.name,
    Type.TEXT.name,
    Type.TEXT.name
]

SUBTRACTION_CAST = [
    Type.INT.name,
    Type.DECIMAL.name,
    None,
    Type.DECIMAL.name,
    None,
    None,
]

DIVISION_CAST = [
    Type.DECIMAL.name,
    Type.DECIMAL.name,
    None,
    Type.DECIMAL.name,
    None,
    None,
]


MULTIPLICATION_CAST = [
    Type.INT.name,
    Type.DECIMAL.name,
    None,
    Type.DECIMAL.name,
    None,
    None,
]

def find_in_array(value, lst):
    index = -1
    try:
        index = lst.index(value)
    except ValueError:
        index = -1

    return index

def get_binary_type(left, op, right):
    casting_list = []
    if op == '+':
        casting_list = ADDITION_CAST
    elif op == '-':
        casting_list = SUBTRACTION_CAST
    elif op == '*':
        casting_list = MULTIPLICATION_CAST
    elif op == '/':
        casting_list = DIVISION_CAST


    left_type = left.tipo.name if left.tipo is not None else None
    right_type = right.tipo.name if right.tipo is not None else None
    index = find_in_array(f'{left_type}-{right_type}', COMBINATIONS)
    index = index if index != -1 else find_in_array(f'{right_type}-{left_type}', COMBINATIONS)
    type = casting_list[index] if index != -1 else None
    return type

class ExpressionsVisitor(Visitor):

    def __init__(self, environment):
        super().__init__(environment)

    def visitAritmeticas(self, node, environment):
        new_type = get_binary_type(left=node.opIzq, op=node.tipoOp, right=node.opDer)
        if new_type is None:
            self.log_error(msg=f'La operación {node.opIzq.tipo} {node.tipoOp} {node.opDer.tipo} no es posible')
            self.correct = False
        else:
            node.tipo = new_type;
