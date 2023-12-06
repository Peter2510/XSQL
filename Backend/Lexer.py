import re
import ply.lex as lex

errors = []

# Conjunto palabras reservadas
keywords = {
    'SELECT': 'SELECT',
    'FROM': 'FROM',
    'CREATE': 'CREATE',
    'DATA': 'DATA',
    'WHERE': 'WHERE',
    'BASE': 'BASE',
    'TABLE': 'TABLE',
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
    'RETURNS': 'RETURN',
    'BEGIN': 'BEGIN',
    'END': 'END',
    'ALTER': 'ALTER',
    'ADD': 'ADD',
    'DROP': 'DROP',
    'DECLARE': 'DECLARE',
    'SET': 'SET'
}

# Conjunto deTokens
tokens = [
    'POR',
    'SUMA',
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
    'ID',
    'ID_DECLARE'
] + list(keywords.values())

# Patron de los tokens
t_POR = r'\*'
t_SUMA = r'\+'
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

# COMENTARIO

def t_comment(t):
    r'\-\-.*'
    t.lexer.lineno += 1

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

# WHIT_SPACE

t_ignore = " \t\f\v"

# SKIPLINE

def t_skip_line(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')
    
# ERROR

def t_error(t):
    #manejar error
    t.lexer.skip(1)
    print('------------Error lexico',t)

def find_column(inp, tk):
    line_start = inp.rfind('\n', 0, tk.lexpos) + 1
    return (tk.lexpos - line_start) + 1


# Crear instancia del lexer
lexer = lex.lex(reflags=re.IGNORECASE)

# Ingresar la cadena de texto para analizar
texto = '''CREATE FUNCTION Retornasuma(@ProductID int) 
RETURNS int 
AS 
-- Returns the stock level for the product. 
BEGIN 
 DECLARE @ret int; 
 SELECT @ret = SUM(Cantidad) 
 FROM inventario 
 WHERE ProductoId = @ProductID 
 
 IF (@ret == NULL) 
 SET @ret = 0; 
 RETURN @ret; 
END;
'''

# Configurar la entrada del lexer
lexer.input(texto)

# Iterar sobre los tokens generados
while True:
    token = lexer.token()
    if not token:
        break
    print(token)
