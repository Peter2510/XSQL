from enum import Enum
from .visitor import Visitor


class Type(Enum):
    INT = 'int'
    DECIMAL = 'decimal'
    TEXTO = 'texto'


COMBINATIONS = [
    f'{Type.INT.value}-{Type.INT.value}',
    f'{Type.INT.value}-{Type.DECIMAL.value}',
    f'{Type.INT.value}-{Type.TEXTO.value}',
    f'{Type.DECIMAL.value}-{Type.DECIMAL.value}',
    f'{Type.DECIMAL.value}-{Type.TEXTO.value}',
    f'{Type.TEXTO.value}-{Type.TEXTO.value}',
]

ADDITION_CAST = [
    Type.INT.value,
    Type.DECIMAL.value,
    Type.TEXTO.value,
    Type.DECIMAL.value,
    Type.TEXTO.value,
    Type.TEXTO.value
]

SUBTRACTION_CAST = [
    Type.INT.value,
    Type.DECIMAL.value,
    None,
    Type.DECIMAL.value,
    None,
    None,
]

DIVISION_CAST = [
    Type.DECIMAL.value,
    Type.DECIMAL.value,
    None,
    Type.DECIMAL.value,
    None,
    None,
]


MULTIPLICATION_CAST = [
    Type.INT.value,
    Type.DECIMAL.value,
    None,
    Type.DECIMAL.value,
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


    index = find_in_array(f'{left.tipo}-{right.tipo}', COMBINATIONS)
    index = index if index != -1 else find_in_array(f'{right.tipo}-{left.tipo}', COMBINATIONS)
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
