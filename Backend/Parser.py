
from Lexer import tokens, lexer, errores, find_column
import ply.yacc as yacc

from src.expresiones.aritmeticas import Aritmeticas
from src.expresiones.primitivos import Primitivo
from src.instrucciones.createdb import createDB
from src.instrucciones.crearTabla import crearTabla

from src.expresiones.relacional import Relacional
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
    instruccion : crearBaseDatos PUNTO_Y_COMA
                | crearTabla PUNTO_Y_COMA
                | expresion
                | funcion_usuario PUNTO_Y_COMA
    '''
    ### falta manipular
    t[0] = t[1]



## crear BD
def p_crearBaseDatos(t):
    '''
    crearBaseDatos : CREATE DATA BASE ID 
    '''
    ### falta manipular
    t[0] = createDB(t.lineno(1), find_column(input, t.slice[1]),t[4])


## crear BD
def p_crearTabla(t):
    '''
    crearTabla : CREATE TABLE ID PARENTESIS_IZQ tablasEspecifico PARENTESIS_DER
    '''
    ### falta manipular
    t[0] = crearTabla(t.lineno(1), find_column(input, t.slice[1]),t[3], t[5])



## PARA LAS TABLAS MAS ESPECIFICO
def p_tablasEspecifico(t):
    '''
    tablasEspecifico : tablasEspecifico COMA columnaDefinicion
    '''
    t[1].append(t[3])
    t[0] = t[1]

def p_tablasEspecifico2(t):
    '''
    tablasEspecifico :  columnaDefinicion
    '''
    t[0] = [t[1]]

def p_columnaDefinicion(t): # ID INT NOT NULL PRIMARY KEY
    '''
    columnaDefinicion : ID tipo_dato nulidad_parametro restriccion_parametro
    '''
    print("EL TIPO ES ESTE: ",t[1],t[2],t[3],t[4])
    t[0] = [t[1]]
    
    
    
def p_tipo_dato(t):
    '''
    tipo_dato : R_INT
    '''
    t[0] = 'int'

def p_tipo_dato2(t):
    '''
    tipo_dato : R_DECIMAL
    '''
    t[0] = 'decimal'
    
def p_tipo_dato3(t):
    '''
    tipo_dato : R_BIT
    '''
    t[0] = 'bit'
    
def p_tipo_dato4(t):
    '''
    tipo_dato : DATETIME
    '''
    t[0] = 'datetime'
    
def p_tipo_dato5(t):
    '''
    tipo_dato : DATE
    '''
    t[0] = 'date'
    
def p_tipo_dato6(t): #VARCHAR(4)
    '''
    tipo_dato : VARCHAR PARENTESIS_IZQ expresion PARENTESIS_DER
    '''
    t[0] = f'VARCHAR({t[3].valor})'
    
def p_tipo_dato7(t):
    '''
    tipo_dato : NVARCHAR PARENTESIS_IZQ expresion PARENTESIS_DER
    '''
    t[0] = f'NVARCHAR({t[3].valor})'
    
def p_tipo_dato8(t):
    '''
    tipo_dato : NCHAR PARENTESIS_IZQ expresion PARENTESIS_DER
    '''
    t[0] = f'NCHAR({t[3].valor})'
        
    
def p_nulidad_parametro(t): # si es null es 1
    '''
    nulidad_parametro : NULL
    '''
    t[0] = '1'

def p_nulidad_parametro2(t): # si es not null es 2
    '''
    nulidad_parametro : NOT NULL
    '''
    t[0] = '0'
    
def p_nulidad_parametro3(t):# si es vacio puede ser null entonces es 1
    '''
    nulidad_parametro : 
    '''
    t[0] = '1'
    
def p_restriccion_parametro(t): #primary -> 1
    '''
    restriccion_parametro : PRIMARY KEY
    '''
    t[0] = '0'

def p_restriccion_parametro2(t): # foranea -> 2
    '''
    restriccion_parametro : REFERENCES ID
    '''
    t[0] = f'forenea({t[2]})'
    

def p_restriccion_parametro3(t): #normal -> 0
    '''
    restriccion_parametro : 
    '''
    t[0] = '0'

#### expresiuones nativas


def p_expRelacional(t):
    '''
    expresion : expresion MENOR_QUE expresion
                | expresion MAYOR_QUE expresion
                | expresion MENOR_O_IGUAL_QUE expresion
                | expresion MAYOR_O_IGUAL_QUE expresion
                | expresion COMPARACION expresion
                | expresion DISTINTO expresion
    '''
    if (t[2] == '<'):
        t[0] = Relacional(t.lineno(2), find_column(input, t.slice[2]), t[1], t[3], '<')
    elif (t[2] == '>'):
        t[0] = Relacional(t.lineno(2), find_column(input, t.slice[2]), t[1], t[3], '>')
    elif (t[2] == '<='):
        t[0] = Relacional(t.lineno(2), find_column(input, t.slice[2]), t[1], t[3], '<=')
    elif (t[2] == '>='):
        t[0] = Relacional(t.lineno(2), find_column(input, t.slice[2]), t[1], t[3], '>=')
    elif (t[2] == '!='):
        t[0] = Relacional(t.lineno(2), find_column(input, t.slice[2]), t[1], t[3], '!=')
    elif (t[2] == '=='):
        t[0] = Relacional(t.lineno(2), find_column(input, t.slice[2]), t[1], t[3], '==')

def p_logica(t):
    '''
    expresion : expresion AND expresion
                | expresion OR expresion
    '''

    if (t[2] == '&&'):
        t[0] = t[1]
    elif (t[2]== '||'):
        t[0]=t[1]



def p_expAritmetica(t):
    '''
    expresion : expresion MAS expresion
                | expresion MENOS expresion
                | expresion POR expresion
                | expresion DIVISION expresion
                | PARENTESIS_IZQ expresion PARENTESIS_DER
    '''
    if (t[2] == '+'):
        t[0] = Aritmeticas(t.lineno(2), find_column(input, t.slice[2]), t[1], t[3], '+')
    elif (t[2] == '-'):
        t[0] = Aritmeticas(t.lineno(2), find_column(input, t.slice[2]), t[1], t[3], '-')
    elif (t[2] == '*'):
        t[0] = Aritmeticas(t.lineno(2), find_column(input, t.slice[2]), t[1], t[3], '*')
    elif (t[2] == '/'):
        t[0] = Aritmeticas(t.lineno(2), find_column(input, t.slice[2]), t[1], t[3], '/')
    elif (t[1] == '(' and t[3] == ')' ):
        t[0] =t[2]
### para enteros 
def p_exp_entero(t):
    '''expresion : ENTERO'''
    ### como funciones le mandas lo que es digamos
    t[0]=Primitivo(t.lineno(1), find_column(input, t.slice[1]),int(t[1]),'int')
## para decimalees
def p_exp_decimal(t):
    '''expresion : DECIMAL'''
    t[0] = Primitivo(t.lineno(1), find_column(input, t.slice[1]),float(t[1]),'decimal')

##para cadenas
def p_exp_cadena(t):
    '''expresion : STR'''
    t[0]=Primitivo(t.lineno(1), find_column(input, t.slice[1]),str(t[1]),'texto')

#id varialbe
def p_exp_cadena(t):
    '''expresion : ID_DECLARE'''
    t[0]=Primitivo(t.lineno(1), find_column(input, t.slice[1]),str(t[1]),'id')
##CREATE DATA BASE
##CREATE TABLE
##CREATE PROD
##CREATE FUNC

        ########################## SSL

        #FUNCIONES

def p_funcion_usuario(t):
    ''' 
    funcion_usuario : CREATE FUNCTION ID PARENTESIS_IZQ parametros_funcion PARENTESIS_DER RETURNS tipo_dato_parametro AS BEGIN sentencias_funciones RETURN expresion PUNTO_Y_COMA END 
    '''
    print('FUNCION DEL USUARIO:',t[3],"parametros",t[5],"tipo dato fn",t[8],t[11],"retorna:",t[13].valor)


##PARAMETROS DE LAS FUNCIONES
def p_parametros_funcion(t):
    '''
    parametros_funcion : parametros_funcion parametro_funcion
    '''
    t[1].append(t[3])
    t[0] = t[1]

def p_parametros_funcion2(t):
    '''
    parametros_funcion :  parametro_funcion
    '''
    t[0] = [t[1]]
    
#parametro de una funcion
def p_parametro_funcion(t): # @id tipoDato 
    '''
    parametro_funcion : ID_DECLARE tipo_dato_parametro 
    '''
    t[0] = [t[1]]
    print('parametro funcion',t[1],t[2])
    
#tipo de dato del parametro 
def p_tipo_dato_parametro(t):
    '''
    tipo_dato_parametro : R_INT
                        | R_DECIMAL
                        | R_BIT
    '''
    t[0] = t[1]
    
    
#sentencias de las funciones
def p_sentencias_funciones(t):
    '''
    sentencias_funciones : sentencias_funciones sentencia_funcion
    '''
    t[1].append(t[2])
    t[0] = t[1]

#sentencia de las funciones
def p_sentencias_funciones1(t):
    '''
    sentencias_funciones : sentencia_funcion
    '''
    t[0] = [t[1]]
    
def p_sentencia_funcion(t):
    '''
    sentencia_funcion : declaracion_variable
    '''
    t[0] = [t[1]]
    
def p_declaracion_variable(t):
    '''
    declaracion_variable : DECLARE ID_DECLARE tipo_dato_parametro PUNTO_Y_COMA
    '''
    t[0] = [t[1]]
    print("declaracion varialbe",t[2],t[3])
    


#PROCEDIMIENTOS

# IF

# CASE


## metodo de error
def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")


## generacion del parser
input = ''

def parse(inp):
    global errores
    global parser
    errores = []
    parser = yacc.yacc()
    global input
    input = inp
    lexer.lineno = 1
    return parser.parse(inp)


data = '''
CREATE FUNCTION Retornasuma(@ProductID int) 
RETURNS int 
AS 
-- Returns the stock level for the product. 
BEGIN 
DECLARE @a int; 
DECLARE @b int; 
DECLARE @c int; 
DECLARE @d int; 
DECLARE @e int; 
RETURN @ret;
END;

CREATE FUNCTION pedr(@ProductID int) 
RETURNS int 
AS 
-- Returns the stock level for the product. 
BEGIN 
DECLARE @a int; 
DECLARE @b int; 
DECLARE @c int; 
DECLARE @d int; 
DECLARE @e int; 
RETURN @ret;
END;
'''

# prueba


instrucciones = parse(data.lower())

## ciclo para que muestre
##for ist in instrucciones:
##    ist.interpretar(None)
#instrucciones[1].interpretar(None, None)