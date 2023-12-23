import re
from src.ejecucion.error import T_error 
import ply.lex as lex
import datetime

errors = []

# Conjunto palabras reservadas
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
    "subtraer":"SUBSTRAER",
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
    'or': 'SQL_OR'
}



tokens = [
    'POR',
    'MAS',
    'DIVISION',
    'MENOS',
    'ASIGNACION',
    'COMPARACION',
    'DISTINTO',
    'PUNTO',
    'COMA',
    'PUNTO_Y_COMA',
    'DOS_PUNTOS',
    'MENOR_QUE',
    'MAYOR_QUE',
    'MENOR_O_IGUAL_QUE',
    'MAYOR_O_IGUAL_QUE',
    'PARENTESIS_IZQ',
    'PARENTESIS_DER',
    'LLAVE_IZQ',
    'LLAVE_DER',
    'OR',
    'AND',
    'NOT',
    'NEGACION',
    'CORCHETE_IZQ',
    'CORCHETE_DER',
    'STR',
    'BITPRIM',
    'DATETIMEPRIM',
    'DATEPRIM',
    'DECIMAL',
    'ENTERO',
    'ID_DECLARE',
    'ID',
    'ARROBA',
    'COMILLASIMPLE',
]+ list(keywords.values())


# Patron de los tokens
t_POR = r'\*'
t_MAS = r'\+'
t_DIVISION = r'\/'
t_MENOS = r'\-'
t_ASIGNACION = r'\='
t_COMPARACION = r'\=\='
t_DISTINTO = r'\!\='
t_PUNTO = r'\.'
t_COMA = r'\,'
t_PUNTO_Y_COMA = r'\;'
t_DOS_PUNTOS = r'\:'
t_MENOR_QUE = r'\<'
t_MAYOR_QUE = r'\>'
t_MENOR_O_IGUAL_QUE = r'\<\='
t_MAYOR_O_IGUAL_QUE = r'\>\='
t_PARENTESIS_IZQ = r'\('
t_PARENTESIS_DER = r'\)'
t_LLAVE_IZQ = r'\{'
t_LLAVE_DER = r'\}'
t_OR = r'\|\|'
t_AND = r'\&\&'
t_NOT = r'\!'
t_NEGACION = r'\!'
t_CORCHETE_IZQ = r'\['
t_CORCHETE_DER = r'\]'
t_ARROBA = r'\@'
t_COMILLASIMPLE = r"\'"

# COMENTARIO

def t_comment(t):
    r'\-\-.*'
    t.lexer.lineno += 1

# IDENTIFICAR CADENAS DE TEXTO CON  COMILLAS DOBLES


# ID NORMAL

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = keywords.get(t.value, 'ID')
    return t

# ID DECLARE

def t_ID_DECLARE(t):
    r'@[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = keywords.get(t.value, 'ID_DECLARE')
    return t


# para las fechas

# Token DATETIME
def t_DATETIMEPRIM(t):
    r'\'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\''
    try:
        t.value = datetime.datetime.strptime(t.value[1:-1], '%Y-%m-%d %H:%M:%S')
    except ValueError:
        print("Error en la fecha y hora")
        errors.append(T_error("Lexico",t.value,"Error en la fecha u hora", t.lexer.lineno, t.lexpos - lexer.lexdata.rfind('\n', 0, t.lexpos)))
        t.value = None
    return t

def t_DATEPRIM(t):
    r'\'\d{4}-\d{2}-\d{2}\''
    try:
        t.value = datetime.datetime.strptime(t.value[1:-1], '%Y-%m-%d').date()
    except ValueError:
        print("Error en la fecha")
        errors.append(T_error("Lexico",t.value,"Error en la fecha", t.lexer.lineno, t.lexpos - lexer.lexdata.rfind('\n', 0, t.lexpos)))
        t.value = None
    return t

## DECIMALES
def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("error en el decimal %d", t.value)
        errors.append(T_error("Lexico",t.value,"Valor del decimal demasiado grande", t.lexer.lineno, t.lexpos - lexer.lexdata.rfind('\n', 0, t.lexpos)))
        t.value = 0
    return t

# ENTERO
def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
         print("Valor del entero demasiado grande %d", t.value)
         errors.append(T_error("Lexico",t.value,"Valor del entero demasiado grande", t.lexer.lineno, t.lexpos - lexer.lexdata.rfind('\n', 0, t.lexpos)))
         t.value = 0
    return t

## para bits
def t_BITPRIM(t):
    r'1|0|null'
    try:
        if (t.value != None and t.value != 'null'):
            t.value = int(t.value)
        else:
            t.value = 'null'
    except ValueError:
        print("Valor del entero demasiado grande %d", t.value)
        errors.append(T_error("Lexico",t.value,"Valor del entero demasiado grande", t.lexer.lineno, t.lexpos - lexer.lexdata.rfind('\n', 0, t.lexpos)))
        t.value = 0
    return t 


##Nueva linea

def newline(t):
    r'\n'
    t.lexer.lineno +=len(t.value)
    
def t_STR(t):
    r'\"[\s\S]*?\"'
    t.value = t.value[1:-1]
    t.value = t.value.replace('\\"', '\"')
    t.value = t.value.replace("\\'", "\'")
    t.value = t.value.replace('\\\\', '\\')
    t.value = t.value.replace('\\t', '\t')
    t.value = t.value.replace('\\n', '\n')
    return t

        
# WHIT_SPACE
t_ignore = " \t\f\v\n"

def t_error(t):   
    errors.append(T_error("Lexico",lexer.lexdata,"No se reconoce el token", t.lexer.lineno, t.lexpos - lexer.lexdata.rfind('\n', 0, t.lexpos)))
    t.lexer.skip(1)
    
##para columna
def find_column(input_text, token):
    last_cr = input_text.rfind('\n', 0, token.lexpos)
    if last_cr < 0:
        last_cr = 0
    column = (token.lexpos - last_cr) + 1
    return column

# Crear instancia del lexer
lexer = lex.lex(reflags=re.IGNORECASE)

