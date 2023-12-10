
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
                | crear_funcion_usuario PUNTO_Y_COMA
                | crear_procedure
                | llamada_procedure
                | expresion_case
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
    tipo_dato : R_DECIMAL PARENTESIS_IZQ expresion COMA expresion PARENTESIS_DER
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
    restriccion_parametro : REFERENCES ID PARENTESIS_IZQ ID PARENTESIS_DER
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

## para decimales
def p_exp_decimal(t):
    '''expresion : DECIMAL'''
    t[0] = Primitivo(t.lineno(1), find_column(input, t.slice[1]),float(t[1]),'decimal')

##para cadenas
def p_exp_cadena(t):
    '''expresion : STR'''
    t[0]=Primitivo(t.lineno(1), find_column(input, t.slice[1]),str(t[1]),'texto')

## id
def p_exp_id(t):
    '''expresion : ID'''
    t[0]=Primitivo(t.lineno(1), find_column(input, t.slice[1]),str(t[1]),'id')

#id variable
def p_exp_id_declare(t):
    '''expresion : ID_DECLARE'''
    t[0]=Primitivo(t.lineno(1), find_column(input, t.slice[1]),str(t[1]),'id_declare')
    
def p_null(t):
    '''expresion : NULL'''
    t[0]=Primitivo(t.lineno(1), find_column(input, t.slice[1]),str(t[1]),'null')
    

##CREATE DATA BASE
##CREATE TABLE
##CREATE PROD
##CREATE FUNC

        ########################## SSL

        #FUNCIONES

def p_funcion_usuario(t):
    ''' 
    crear_funcion_usuario : CREATE FUNCTION ID PARENTESIS_IZQ parametros_funcion PARENTESIS_DER RETURNS tipo_dato_parametro AS BEGIN sentencias_funciones END 
    '''
    print('FUNCION DEL USUARIO:',t[3],"parametros",t[5],"tipo dato fn",t[8],t[11])


##PARAMETROS DE LAS FUNCIONES
def p_parametros_funcion(t):
    '''
    parametros_funcion : parametros_funcion  COMA parametro_funcion
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
    '''
    t[0] = t[1]
    
#tipo de dato de la variable
def p_tipo_dato_variable_funcion(t):
    '''
    tipo_dato_variable : tipo_dato
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
    
#sentecias dentro de las funciones    
def p_sentencia_funcion(t):
    '''
    sentencia_funcion : declaracion_variables
                    | set_variable_funcion
                    | return
                    | expresion_if
    '''
    t[0] = [t[1]]
    
#declare varias variables
def p_declaracion_variables(t):
    '''
    declaracion_variables :  DECLARE lista_declaracion_variables PUNTO_Y_COMA
    '''
    t[0] = t[1]
      
    
#lista de declaracion de variables
def p_lista_declaracion_variables(t):
    '''
    lista_declaracion_variables : lista_declaracion_variables COMA declaracion_variable
    '''
    t[1].append(t[3])
    t[0] = t[1]
    
#declaracion de una sola variable    
def p_lista_declaracion_variables2(t):
    '''
    lista_declaracion_variables :  declaracion_variable
    '''
    t[0] = [t[1]]
    
#declarar variable
def p_declaracion_variable(t):
    '''
    declaracion_variable : ID_DECLARE tipo_dato_variable 
    '''
    t[0] = [t[1]]
    print("declaracion varialbe",t[1],t[2])
    
def p_set_variable_funcion(t):
    '''
    set_variable_funcion : SET ID_DECLARE ASIGNACION asignacion_set PUNTO_Y_COMA
    '''
    t[0] = [t[1]]
    print("set_variable_funcion","variable:",t[2],"valor:",t[4])
    
#asignacion set
def p_asignacion_set(t):
    '''
    asignacion_set : expresion
                   | llamada_funcion
    '''
    t[0] = t[1]
    
# RETURN
def p_return(t):
    '''
    return : RETURN expresion PUNTO_Y_COMA
    '''
    t[0] = t[2]
    print("return",t[2])
    
#llamada de una funcion
def p_llamada_funcion(t):
    '''
    llamada_funcion : ID PARENTESIS_IZQ parametros_llamada_funcion PARENTESIS_DER
    '''
    print("llamada_funcion",t[1],"parametros",t[3])
    
#llamada de una funcion
def p_llamada_funcion2(t):
    '''
    llamada_funcion : ID PARENTESIS_IZQ PARENTESIS_DER
    '''
    print("llamada_funcion",t[1]," SIN parametros")
    
#parametros de la llamada de una funcion
def p_parametros_llamada_funcion(t):
    '''
    parametros_llamada_funcion : parametros_llamada_funcion COMA parametro_llamada_funcion
    '''
    t[1].append(t[3])
    t[0] = t[1]

def p_parametros_llamada_funcion2(t):
    '''
    parametros_llamada_funcion :  parametro_llamada_funcion
    '''
    t[0] = [t[1]]
    
#parametro de la llamada de una funcion
def p_parametro_llamada_funcion(t): # id
    '''
    parametro_llamada_funcion : expresion
    '''
    t[0] = [t[1]]
    print('parametro llamada funcion',t[1])
    

    #PROCEDURES
    
def p_procedure(t):
    '''
    crear_procedure : CREATE PROCEDURE ID PARENTESIS_IZQ parametros_procedure PARENTESIS_DER AS BEGIN sentencias_funciones END PUNTO_Y_COMA
    '''
    print("procedure",t[3],"parametros",t[5],t[9])
     
#parametros de los procedures
def p_parametros_procedure(t):
    '''
    parametros_procedure : parametros_procedure COMA parametro_procedure
    '''
    t[1].append(t[3])
    t[0] = t[1]

def p_parametros_procedure2(t):
    '''
    parametros_procedure :  parametro_procedure
    '''
    t[0] = [t[1]]
    
#parametro de un procedure
def p_parametro_procedure(t): # @id tipoDato 
    '''
    parametro_procedure : ID_DECLARE tipo_dato 
    '''
    t[0] = [t[1]]
    print('parametro procedure',t[1],t[2])
    
#llamada procedure
def p_llamada_procedure(t):
    '''
    llamada_procedure : EXEC ID lista_variables_procedure PUNTO_Y_COMA
    '''
    print("llamada_procedure_1",t[2])
    
#lista_variables_procedure
def p_lista_variables_procedure(t):
    '''
    lista_variables_procedure : lista_variables_procedure COMA variable_procedure
    '''
    t[1].append(t[3])
    t[0] = t[1]
    
#lista_variables_procedure
def p_lista_variables_procedure2(t):
    '''
    lista_variables_procedure : variable_procedure
    '''
    t[0] = [t[1]]
    
#variable_procedure
def p_variable_procedure(t):
    '''
    variable_procedure : valor_variable_procedure
    '''
    t[0] = [t[1]]
    print("variable_procedure",t[1])
    
#valor_variable_procedure
def p_valor_variable_procedure(t):
    '''
    valor_variable_procedure : ID_DECLARE ASIGNACION expresion
    '''
    t[0] = t[1]
    print("valor_variable_procedure",t[3])
    
#valor_variable_procedure
def p_valor_variable_procedure2(t):
    '''
    valor_variable_procedure : expresion
    '''
    t[0] = t[1]
    print("valor_variable_procedure",t[1])
                
#if
def p_if(t): 
    '''
    expresion_if : IF expresion THEN cuerpo_if_else END IF PUNTO_Y_COMA
    '''
    t[0] = t[1]
    print("if",t[2],t[4])

def p_if2(t):
    '''
    expresion_if : IF expresion THEN cuerpo_if_else expresion_else END IF PUNTO_Y_COMA
    '''    
    t[0] = t[1]
    print("if",t[2],t[4],t[5])
    
def p_if3(t):
    '''
    expresion_if : IF expresion THEN cuerpo_if_else expresion_else_if expresion_else END IF PUNTO_Y_COMA
    '''    
    t[0] = t[1]
    print("if",t[2],t[4],t[5],t[6])

def p_if4(t):
    '''
    expresion_if : IF expresion THEN cuerpo_if_else expresion_else_if END IF PUNTO_Y_COMA
    '''
    t[0] = t[1]
    print("if",t[2],t[4],t[5])

# cuerpo del if
def p_cuerpo_if_else(t):
    '''
    cuerpo_if_else : sentencias_funciones
    '''
    t[0] = t[1]
    
# expresion else
def p_expresion_else(t):
    '''
    expresion_else : ELSE cuerpo_if_else
    '''
    t[0] = t[2]

# expresion else if
def p_expresion_else_if(t):
    '''
    expresion_else_if : ELSEIF expresion THEN cuerpo_if_else
    '''
    t[0] = t[4]


#case 
def p_expresion_case(p):
    '''
    expresion_case : CASE when_clauses ELSE expresion END expresion
    '''
    p[0] = p[4]
    print("en case con else")
    
#case 2
def p_expresion_case2(p):
    '''
    expresion_case : CASE when_clauses END expresion
    '''
    p[0] = p[4]
    print("en case sin else")

def p_when_clauses(p):
    '''
    when_clauses : WHEN expresion THEN expresion
                 | when_clauses WHEN expresion THEN expresion
    '''
    p[0] = (p[2], p[4]) if len(p) == 5 else (p[2], p[4], p[1])
    

## metodo de error
def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value,p.lineno,find_column(input, p))
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

CASE 
    WHEN 1==1 
        THEN 'UNO IGUAL 1'
    WHEN 1==2 
        THEN 'UNO IGUAL 2'
    WHEN 1==3 
        THEN 'UNO IGUAL 3'
    WHEN 1==4 
        THEN 'UNO IGUAL 4'
    else 'NADA'
    END validacion

'''

# prueba

instrucciones = parse(data.lower())

## ciclo para que muestre
##for ist in instrucciones:
##    ist.interpretar(None)
#instrucciones[1].interpretar(None, None)