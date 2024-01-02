import ply.lex as lex
import ply.yacc as yacc
from src.C3D.c3d import Nodo

keywords = {
    'create': 'CREATE',
    'data': 'DATA',
    'base': 'BASE',
    'table': 'TABLE',
    'alter': 'ALTER',
    'drop': 'DROP',
    'column': 'COLUMN',
    'truncate': 'TRUNCATE',
    'usar': 'USAR',
        
        
    'select': 'SELECT',
    'from': 'FROM',   
    'where': 'WHERE',
    "update":"UPDATE",
    "insert":"INSERT",
    "delete":"DELETE",
    
    "concatena":"CONCATENA",
    "substraer":"SUBSTRAER",
    "hoy":"HOY",
    "contar":"CONTAR",
    "suma":"SUMA",
    "cas":"CAS",
    
    'null': 'NULL',
    'primary': 'PRIMARY',
    'foreing': 'FOREING',
    'key': 'KEY',
    'reference': 'REFERENCE',
    
    'procedure': 'PROCEDURE',
    'as': 'AS',
    'exec': 'EXEC',
    'function': 'FUNCTION',
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE',
    'endif': 'ENDIF',
    'elseif': 'ELSEIF',
    'return': 'RETURN',
    'returns': 'RETURNS',
    'begin': 'BEGIN',
    'case': 'CASE',
    'when': 'WHEN',
    'end': 'END',
    'add': 'ADD',
    'declare': 'DECLARE',
    'set': 'SET',
    
    'varchar': 'VARCHAR',
    'nchar': 'NCHAR',
    'nvarchar': 'NVARCHAR',
    'int': 'R_INT',
    'bit': 'R_BIT',
    'decimal': 'R_DECIMAL',

    'datetime': 'DATETIME',
    'date': 'DATE',
    
    'foreign': 'FOREIGN',

    'into': 'INTO',
    'values': 'VALUES',
    'and': 'SQL_AND',
    'or': 'SQL_OR',
    'not': 'SQL_NOT'
}
# Lista de tokens
tokens = [
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'GT',
    'LT',
    'EQ',
    'ID',
]+list(keywords.values())

# Reglas de expresiones regulares para tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_GT = r'\>'
t_LT = r'\<'
t_EQ = r'\=='
t_ignore = " \t\f\v"


# Regla para reconocer números
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = keywords.get(t.value, 'ID')
    return t


# Regla para manejar saltos de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Construcción del lexer
lexer = lex.lex()

## la parte del parse
temp = 0
def temporal():
    global temp
    return temp


def p_init(t):
    '''
    init : instrucciones
    '''
    t[0] = t[1]


def p_instruccionesListado(t):
    '''
    instrucciones : instrucciones instruccion
    '''
    ## aqui si existe la instruccion
    t[1].append(t[2])
    t[0] = t[1]


def p_instruccionSimple(t):
    '''
    instrucciones : instruccion 
    '''
    t[0]= [t[1]]


def p_instruccionGeneral(t):
    '''
    instruccion : statement

    '''
    ### falta manipular
    t[0] = t[1]


# Reglas de la gramática
def p_statement_if(p):
    '''
    statement : IF LPAREN condition RPAREN THEN expression ENDIF
              | IF LPAREN condition  RPAREN THEN expression ELSE expression ENDIF
              | expression
    '''
    if len(p) == 8:
        p[0] = f"if ({p[3]}) goto {p[6]}\n"
    elif len(p) == 2:
        p[0] = f't={p[1]}'
    else:
        p[0] = f"if ({p[3]}) goto {p[6]}\nelse goto {p[8]}\n"

def p_expression_binop(p):
    '''
    expression : expression PLUS expression
               | expression MINUS expression
               | expression TIMES expression
               | expression DIVIDE expression
               | LPAREN expression RPAREN
               | NUMBER
               | ID
    '''
    global temp
    if len(p) == 2:
        p[0] = f'({p[1]})'
    elif p[1] == '(':
        p[0] = f"({p[2]})"
    else:
        temp+=1
        gramatica = f"t{str(temporal())}=({p[1]} {p[2]} {p[3]})"
        print( f"t{str(temporal())}=({p[1]} {p[2]} {p[3]})")
        p[0] =Nodo('OPARIT', p[2], [p[1], p[3]], p.lexer.lineno, 0, gramatica)


def p_condition(p):
    '''
    condition : expression GT expression
              | expression LT expression
              | expression EQ expression
    '''
    p[0] = f"({p[1]} {p[2]} {p[3]})"

def p_error(p):
    print(f"Syntax error at token {p.type}", p)

parser = yacc.yacc()

input_text = '''
if (5 > 3) then
    10 * (2 + 3)
endif
44+3*5+3*8
'''

parsed = parser.parse(input_text)
print(parsed)
