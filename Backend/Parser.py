from ply.yacc import  yacc
from Lexer import tokens, lexer, errores, find_column


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