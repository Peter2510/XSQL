from ply.yacc import  yacc
from Lexer import tokens, lexer, errores, find_column
### establecer precedencias 
precedence = (
    ('left', 'MAS','MENOS'),
    ('left', 'POR','DIVISION'),
    ('left', 'COMPARACION','DISTINTO','MENOR_QUE','MAYOR_QUE','MENOR_O_IGUAL_QUE', 'MAYOR_O_IGUAL_QUE'),
    ('left', 'OR','AND'),
    ('left', 'PARENTESIS_IZQ','PARENTESIS_DER')
);


## ahora el parser general s
##############
### SECCION GENERAL DE LAS INSTRUCCIONES
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

def p_instruccionGeneral(t):
    '''
    instruccion : createEspecifico PUNTO_Y_COMA
                | alterEspecifico PUNTO_Y_COMA
                | dropEspecifico PUNTO_Y_COMA
                | truncateEspecifico PUNTO_Y_COMA
    '''
    t[0] = t[1]

##############

### SECCION PARA CREAR
def p_createEspecifico(t):
    '''
        createEspecifico :  CREATE createIndividual
    '''
    t[0] = t[2]


def p_createTablas(t):
    '''
    createIndividual : TABLE expresion PARENTESIS_IZQ tablasEspecifico PARENTESIS_DER
    '''
def p_createDatabase(t):
    '''
    createIndividual : DATA BASE expresion
    '''



### DE ESTOS FALTA LA SENTENCIA RECURSIVA
def p_createProcedimiento(t):
    '''
    createIndividual : PROCEDURE expresion PARENTESIS_IZQ parametros PARENTESIS_DER AS
    '''  

def p_createFuncion(t):
    '''
    createIndividual : FUNCTION expresion PARENTESIS_IZQ parametros PARENTESIS_DER RETURN tipodato AS BEGIN END 
    '''    
##############
## PARA LAS TABLAS MAS ESPECIFICO
def p_tablasEspecifico(t):
    '''
    tablasEspecifico : tablasEspecifico COMA crearSentenciaTabla
                        |  crearSentenciaTabla
    '''



def p_crearElementos(t):
    '''
    crearSentenciaTabla : creacionNormalArtributoTabla 
                        |  creacionLlaveForanea
    '''


def p_creacionNormalArtributoTabla(t):
    '''
         creacionNormalArtributoTabla : expresion tipodato nulidad opcionllaveprimaria
    '''


def p_opcionllaveprimaria(t):
    '''
    opcionllaveprimaria : PRIMARY KEY 
                        | 
    '''


def p_creacionLlaveForanea(t):
    '''
    creacionLlaveForanea : FOREING KEY PARENTESIS_IZQ expresion PARENTESIS_DER REFERENCE expresion PARENTESIS_IZQ expresion PARENTESIS_DER
    '''
##############
##############
### SECCION DE PARAMETROS
def p_parametros(t):
    '''
    parametros : p_parametrosEspecifico
                | 
    '''
def p_parametrosEspecifico(t):
    '''
    p_parametrosEspecifico : p_parametrosEspecifico COMA ARROBA expresion tipodato
                            | ARROBA expresion tipodato
    '''





##############
##############
## SECCION DEL ALTER

##############
## para los tipos de datos 

def p_tipodato(t):
    '''
    tipodato : INT
             | BIT
             | opcionChar
             | DATETIME
             | DATE
    '''

## para los chars
def p_opcionChar(t):
    '''
    opcionChar : NCHAR PARENTESIS_IZQ expresion PARENTESIS_DER
                | NVARCHAR PARENTESIS_IZQ expresion PARENTESIS_DER 
    '''


## ahora aqui la nulalidad 
def p_nulidad(t):
    '''
    nulidad : posiblenull NULL 
            |  
    '''
def p_posiblenull(t):
       '''
    posiblenull : NOT  
                  |  
    ''' 
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



#### expresiuones nativas

### para enteros 
def p_exp_entero(t):
    '''expresion : ENTEROS'''
    ### como funciones le mandas lo que es digamos
    t[0]= primitivos(t.lineno(1), find_column(input, t.slice[1]),int(t[1]),'number')
## para decimalees
def p_exp_decimal(t):
    '''expresion : DECIMALES'''
    t[0] = primitivos(t.lineno(1), find_column(input, t.slice[1]),float(t[1]),'number')

##para cadenas
def p_exp_cadena(t):
    '''expresion : CADENAS'''
    t[0]=primitivos(t.lineno(1), find_column(input, t.slice[1]),str(t[1]),'string')


############################################################################################################################
############################################################################################################################
############################################################################################################################
############################################################################################################################
############################################################################################################################
############################################################################################################################
# Parser ESTO PARA EL XML
def p_element(p):
    '''element : TAGABIERTO attributes TAGCERRADO
               | TAGABIERTO TAGCERRADO'''
    pass

def p_attributes(p):
    '''attributes : ATRIBUTOSTAG attributes
                  | ATRIBUTOSTAG'''
    pass



## metodo de error
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
CREATE DATA BASE "hola";
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