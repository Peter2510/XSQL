import ply.yacc as yacc
from Lexer import tokens, lexer, errores, find_column

## establecer precedencias 

precedence = (
    ('left', 'MAS','MENOS'),
    ('left', 'POR','DIVISION'),
    ('left', 'COMPARACION','DISTINTO','MENOR_QUE','MAYOR_QUE','MENOR_O_IGUAL_QUE', 'MAYOR_O_IGUAL_QUE'),
    ('left', 'OR','AND'),
    ('left', 'PARENTESIS_IZQ','PARENTESIS_DER'),
    ('left', 'AS')
);


## ahora el parser general s
##############
### SECCION GENERAL DE LAS INSTRUCCIONES
def p_init(t):
    '''
    init : 
    '''
    t[0] = t[1]
    



## metodo de error
def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")


## generacion del parser
input = ''

def parse(inp):
    global errors
    global parser
    errors = []
    parser = yacc.yacc()
    global input
    input = inp
    lexer.lineno = 1
    return parser.parse(inp)
