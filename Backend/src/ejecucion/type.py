from enum import Enum

class Type(Enum):
    INT = 0
    BIT = 1
    DECIMAL = 2
    DATE = 3
    DATETIME = 4  
    NCHAR = 5
    NVARCHAR = 6
    VARCHAR = 7    
    NULL = 8
    ID = 9
    IDDECLARE = 10    
    TEXT = 11
    VOID = 12

class OperationType(Enum):
    SUMA = 0
    RESTA = 1
    MULTIPLICACION = 2
    DIVISION = 3
    MAYOR_IGUAL = 4
    MENOR_IGUAL = 5
    MAYOR = 6
    MENOR = 7
    IGUAL = 8
    DISTINTO = 9
    AND = 10
    OR = 11