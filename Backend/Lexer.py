import re 
import ply.lex as lex
import datetime

errores = []
errors = []

# Conjunto palabras reservadas
keywords = {
    'CREATE': 'CREATE',
    'DATA': 'DATA',
    'BASE': 'BASE',
    'TABLE': 'TABLE',
    'ALTER': 'ALTER',
    'DROP': 'DROP',
    'TRUNCATE': 'TRUNCATE',
        
        
    'SELECT': 'SELECT',
    'FROM': 'FROM',   
    'WHERE': 'WHERE',
    "UPDATE":"UPDATE",
    "INSERT":"INSERT",
    "DELETE":"DELETE",
    
    "CONCATENA":"CONCATENA",
    "SUBSTRAER":"SUBSTRAER",
    "HOY":"HOY",
    "CONTAR":"CONTAR",
    "SUMA":"SUMA",
    "CAS":"CAS",
    
    'NOT': 'NOT',
    'NULL': 'NULL',
    'PRIMARY': 'PRIMARY',
    'FOREING': 'FOREING',
    'KEY': 'KEY',
    'REFERENCE': 'REFERENCE',
    'VARCHAR': 'VARCHAR',
    'PROCEDURE': 'PROCEDURE',
    'AS': 'AS',
    'EXEC': 'EXEC',
    'FUNCTION': 'FUNCTION',
    'IF': 'IF',
    'RETURN': 'RETURN',
    'RETURNS': 'RETURNS',
    'BEGIN': 'BEGIN',
    'END': 'END',
    'ADD': 'ADD',
    'DECLARE': 'DECLARE',
    'SET': 'SET',
   
    'BIT': 'BIT',
    'Nchar': 'NCHAR',
    'Nvarchar': 'NVARCHAR',
    'Datetime': 'DATETIME',
    'Date': 'DATE',
    'PRIMARY' :'PRIMARY',
    'REFERENCES': 'REFERENCES',
    'FOREIGN': 'FOREIGN'    
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
    'NEGACION',
    'CORCHETE_IZQ',
    'CORCHETE_DER',
    'STR',
    'BITPRIM',
    'DECIMAL',
    'ENTERO',
    'ID_DECLARE',
    'ID',
    'ARROBA'
]+ list(keywords.values())


# Patron de los tokens
t_POR = r'\*'
t_MAS = r'\+'
t_DIVISION = r'\/'
t_MENOS = r'\-'
t_ASIGNACION = r'\='
t_COMPARACION = r'\=\='
t_DISTINTO = r'\!\=\='
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
t_NEGACION = r'\!'
t_CORCHETE_IZQ = r'\['
t_CORCHETE_DER = r'\]'
t_ARROBA = r'\@'

# COMENTARIO

def t_comment(t):
    r'\-\-.*'
    t.lexer.lineno += 1

# IDENTIFICAR CADENAS DE TEXTO CON  COMILLAS DOBLES Y SIMPLES    

def t_STR(t):
    r'(\"[\s\S]*?\")|(\'[\s\S]*?\')|(\`[\s\S]*?\`)'
    t.value = t.value[1:-1]
    t.value = t.value.replace('\\"', '\"')
    t.value = t.value.replace("\\'", "\'")
    t.value = t.value.replace('\\\\', '\\')
    t.value = t.value.replace('\\t', '\t')
    t.value = t.value.replace('\\n', '\n')
    return t

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

## DECIMALES
def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("error en el decimal %d", t.value)
        t.value = 0
    return t

# ENTERO
def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
         print("Valor del entero demasiado grande %d", t.value)
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
        t.value = 0
    return t 


# para las fechas

# Token DATETIME
def t_DATETIMEPRIM(t):
    r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}'
    try:
        t.value = datetime.datetime.strptime(t.value, '%Y-%m-%d %H:%M:%S')
    except ValueError:
        print("Error en la fecha y hora")
        t.value = None
    return t


def t_DATEPRIM(t):
    r'\d{4}-\d{2}-\d{2}'
    try:
        t.value = datetime.datetime.strptime(t.value, '%Y-%m-%d').date()
    except ValueError:
        print("Error en la fecha")
        t.value = None
    return t


##Nueva linea

def newline(t):
    r'\n'
    t.lexer.lineno +=len(t.value)


## PARA LOS TAGS DEL XML
# def t_TAGABIERTO(t):
#     r'<[A-Za-z]+>'
#     return t

# def t_TAGCERRADO(t):
#     r'</[A-Za-z]+>'
#     return t

# def t_ATRIBUTOSTAG(t):
#     r'[A-Za-z]+="[^"]*"'
#     return t


        #ignora lo demas
        
# WHIT_SPACE
t_ignore = " \t\f\v"
def t_error(t):
    
    t.lexer.skip(1)
    
##para columna
def find_column(inp, tk):
    line_start = inp.rfind('\n', 0, tk.lexpos)+1
    return (tk.lexpos-line_start)+1


# Crear instancia del lexer
lexer = lex.lex(reflags=re.IGNORECASE)

# # Ingresar la cadena de texto para analizar
# texto = 'SELECT : '

# # Configurar la entrada del lexer
# lexer.input(texto)

# # Iterar sobre los tokens generados
# while True:
#     token = lexer.token()
#     if not token:
#         break
#     print(token)