from enum import Enum
from src.ejecucion.type import Type
from src.visitor.visitor import Visitor

COMBINATIONS = [

    f'{Type.BIT.name}-{Type.BIT.name}',
    f'{Type.BIT.name}-{Type.INT.name}',
    f'{Type.BIT.name}-{Type.DECIMAL.name}',
    f'{Type.BIT.name}-{Type.DATE.name}',
    f'{Type.BIT.name}-{Type.DATETIME.name}',
    f'{Type.BIT.name}-{Type.TEXT.name}',
    f'{Type.BIT.name}-{Type.BOOLEAN.name}',
    f'{Type.INT.name}-{Type.INT.name}',
    f'{Type.INT.name}-{Type.DECIMAL.name}',
    f'{Type.INT.name}-{Type.DATE.name}',
    f'{Type.INT.name}-{Type.DATETIME.name}',
    f'{Type.INT.name}-{Type.TEXT.name}',
    f'{Type.INT.name}-{Type.BOOLEAN.name}',
    f'{Type.DECIMAL.name}-{Type.DECIMAL.name}',
    f'{Type.DECIMAL.name}-{Type.DATE.name}',
    f'{Type.DECIMAL.name}-{Type.DATETIME.name}',
    f'{Type.DECIMAL.name}-{Type.TEXT.name}',
    f'{Type.DECIMAL.name}-{Type.BOOLEAN.name}',
    f'{Type.DATE.name}-{Type.DATE.name}',
    f'{Type.DATE.name}-{Type.DATETIME.name}',
    f'{Type.DATE.name}-{Type.TEXT.name}',
    f'{Type.DATE.name}-{Type.BOOLEAN.name}',
    f'{Type.DATETIME.name}-{Type.DATETIME.name}',
    f'{Type.DATETIME.name}-{Type.TEXT.name}',
    f'{Type.DATETIME.name}-{Type.BOOLEAN.name}',
    f'{Type.TEXT.name}-{Type.TEXT.name}',
    f'{Type.TEXT.name}-{Type.BOOLEAN.name}',
    f'{Type.BOOLEAN.name}-{Type.BOOLEAN.name}'
]

ADDITION_CAST = [
    Type.BIT,
    Type.INT,
    Type.DECIMAL,
    None,
    None,
    Type.TEXT,
    None,
    Type.INT,
    Type.DECIMAL,
    None,
    None,   
    Type.TEXT,
    None,
    Type.DECIMAL,
    None,
    None,
    Type.TEXT,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    Type.TEXT,
    None,    
    None
]

SUBTRACTION_CAST = [
    None,
    Type.INT,
    Type.DECIMAL,
    None,
    None,
    None,
    None,
    
    Type.INT,
    Type.DECIMAL,
    None,
    None,   
    None,
    None,
    
    Type.DECIMAL,
    None,
    None,
    None,
    None,
    
    None,
    None,
    None,
    None,
    
    None,
    None,
    None,
    
    None,
    None,
    
    None
]

MULTIPLICATION_CAST = [
    Type.BIT,
    Type.INT,
    Type.DECIMAL,
    None,
    None,
    None,
    None,
    
    Type.INT,
    Type.DECIMAL,
    None,
    None,   
    None,
    None,
    
    Type.DECIMAL,
    None,
    None,
    None,
    None,
    
    None, 
    None,
    Type.TEXT,
    None,
    
    None, 
    Type.TEXT,
    None, 
    
    None, 
    None,
    
    None
]

DIVISION_CAST = [
    Type.BIT,
    Type.INT,
    Type.DECIMAL,
    None,
    None,
    None,
    None,
    
    Type.INT,
    Type.DECIMAL,
    None,
    None,   
    None,
    None,
    
    Type.DECIMAL,
    None,
    None,
    None,
    None,
    
    None, 
    None,
    Type.TEXT,
    None,
    
    None, 
    Type.TEXT,
    None, 
    
    None, 
    None,
    
    None
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
            environment.addError('Semántico', "" ,f'La operación {node.opIzq.tipo} {node.tipoOp} {node.opDer.tipo} no es posible', node.fila, node.columna)
            self.correct = False
            print(f'La operación {node.opIzq.tipo} {node.tipoOp} {node.opDer.tipo} no es posible')
        else:
            node.tipo = new_type
            print("CORRECTO")
