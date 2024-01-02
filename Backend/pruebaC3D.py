import ply.lex as lex
import ply.yacc as yacc

# Lista de tokens
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'GT',
    'LT',
    'EQ',
    'IF',
    'ELSE',
    'ENDIF',
    'THEN',
    'OR', 
    'AND'
)

# Reglas de expresiones regulares para tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_GT = r'>'
t_LT = r'<'
t_EQ = r'=='
t_IF = r'if'
t_ELSE = r'else'
t_ENDIF = r'endif'
t_THEN = r'then'
t_AND = r'and'
t_OR = r'or'
t_ignore = ' \t'

# Regla para reconocer números
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
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

def p_statement_if(p):
    '''
    statement : IF condition THEN expression ENDIF
              | IF condition THEN expression ELSE expression ENDIF
    '''
    if len(p) == 6:
        p[0] = f"if ({p[2]}) goto {p[4]}\n"
    else:
        p[0] = f"if ({p[2]}) goto {p[4]}\nelse goto {p[6]}\n"

def p_condition_expression_binop(p):
    '''
    condition : condition GT condition
              | condition LT condition
              | condition EQ condition
              | condition AND condition
              | condition OR condition
              | expression
    '''
    if len(p) == 4:
        p[0] = f"({p[1]} {p[2]} {p[3]})"
    else:
        p[0] = p[1]

def p_expression_binop(p):
    '''
    expression : expression PLUS expression
               | expression MINUS expression
               | expression TIMES expression
               | expression DIVIDE expression
    '''
    p[0] = f"({p[1]} {p[2]} {p[3]})"

def p_expression_number(t):
    '''
    expression : NUMBER
    '''
    t[0] = str(t[1])

# ... definición de otras reglas gramaticales ...

def p_error(p):
    print(f"Syntax error at token {p.type}")

parser = yacc.yacc()

f = open("./entrada.txt", "r")
input = f.read()
print(input)
cad=parser.parse(input)
print(cad)




    