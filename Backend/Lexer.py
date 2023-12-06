import re 
import ply.lex as lex


errores = []

reserved = {

}


tokens = [
    'MAYOR',
    'MENOR',
    'DIV',
    'ENTEROS',
    'DECIMALES',
    'CADENAS',
    'ID',
    'TAGABIERTO',
    'TAGCERRADO',
    'ATRIBUTOSTAG',
]



### EXPRESIONES --------
## decimales
def t_DECIMALES(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("error en el decimal")
        t.value = 0
    return t
##  para enteros
#Entero
def t_ENTEROS(n):
    r'\d+'
    try:
        if(n.value != None):
            n.value = int(n.value)
        else:
            n.value = 'nothing'
    except ValueError:
        print("Valor del entero demasiado grande %d", n.value)
        n.value = 0
    return n

# para cadenas
def t_CADENAS(t):
    r'(\".*?\")'
    ##qiita comiillas
    t.value = t.value[1:-1]
    ##remplaza valores
    t.value = t.value.replace('\\t', '\t')
    t.value = t.value.replace('\\n', '\n')
    t.value = t.value.replace('\\"', '\"')
    t.value = t.value.replace("\\'", "\'")
    t.value = t.value.replace('\\\\', '\\')
    return t
# para identtificadors
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    #determina en el diccionario el id
    t.type = reserved.get(t.value, 'ID')
    return t
##comentario de linea
def t_comentarioSimple(t):
    r'\-\-.*'
    ## solo agrega
    t.lexer.lineno+=1


    ##nueva linea

def newline(t):
    r'\n'
    t.lexer.lineno +=len(t.value)


## PARA LOS TAGS DEL XML
def t_TAGABIERTO(t):
    r'<[A-Za-z]+>'
    return t

def t_TAGCERRADO(t):
    r'</[A-Za-z]+>'
    return t

def t_ATRIBUTOSTAG(t):
    r'[A-Za-z]+="[^"]*"'
    return t


    #ignora lo demas
t_ignore = " \t"

def t_error(t):
    t.lexer.skip(1)
##para columna
def find_column(inp, tk):
    line_start = inp.rfind('\n', 0, tk.lexpos)+1
    return (tk.lexpos-line_start)+1




lexer = lex.lex(reflags = re.IGNORECASE)