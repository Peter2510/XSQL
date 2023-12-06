from ply.yacc import  yacc
from Lexer import tokens, lexer, errores, find_column
### establecer precedencias 

precedence = (
    ('left', 'MAS','MENOS'),
    ('left', 'POR','DIVISION'),
    ('left', 'COMPARACION','DISTINTO','MENOR_O_IGUAL_QUE', 'MAYOR_O_IGUAL_QUE'),
    ('left', 'OR','AND'),
    ('left', 'PARENTESIS_IZQ','PARENTESIS_DER')
);


## ahora el parser general
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
    if (t[2]!= ""):
        t[1].append(t[2])
    t[0] = t[1]  # Si t[1] no es una lista, crea una nueva lista con los elementos


def p_instruccionSimple(t):
    '''
    instrucciones : instruccion 
    '''
    if t[1] =="":
        t[0]=[]
    else :
        ### no se te olvie apilar como arreglo y no como objeto
        t[0]= [t[1]]

def instruccionGeneral(t):
    '''
    instruccion : CREATE
                | USE 
    '''
##############
##############


##############
####AHORA PARA LOS OPERADORES##
def p_expresiones(t):
    '''
    expresion : expresion MAS expresion
            |  expresion MENOS expresion
            |  expresion POR expresion
            |  expresion DIVISION expresion
    '''
    if t[2] == '+':
        t[0] = t[1]+t[3]
    elif t[2]=='-':
        t[0]=t[1]-t[3]
    elif t[2]=="*":
        t[0]= t[1]*t[3]
    elif t[2]=='/':
        t[0] = t[1]/t[3]

##############
##############
# Parser ESTO PARA EL XML
def p_element(p):
    '''element : TAGABIERTO attributes TAGCERRADO
               | TAGABIERTO TAGCERRADO'''
    pass

def p_attributes(p):
    '''attributes : ATRIBUTOSTAG attributes
                  | ATRIBUTOSTAG'''
    pass

def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")


## generacion del parser
def parse(inp):
    global errores
    global parser
    errores = []
    parser = yacc.yacc()
    global input
    input = inp
    lexer.lineno = 1
    return parser.parse(inp)

# Data
data = '''
<Bd>
    <Products>
    <Product pid="p123">
        <Name>gizmo</Name>
        <Price>22.99</Price>
    </Product>
    <Product pid="p231">
        <Name>gizmoPlus</Name>
        <Price>99.99</Price>
    </Product>
    </Products>
</Bd>
<Bd>
</Bd>
1
0
2023-12-31
null
2023-12-05 13:45:30
'''

# prueba


def prueba(texto):
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)



lexer.input(data)
prueba(data)