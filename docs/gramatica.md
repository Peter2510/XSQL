#Gramática

## Expresions regulares
¡Entendido! Aquí tienes una breve descripción para las palabras clave y las expresiones regulares de los tokens:

### Palabras Clave:

- **CREATE:** Utilizado para crear objetos en la base de datos, como tablas o procedimientos.
- **DATA:** Referente a la manipulación de datos en la base de datos.
- **BASE:** Relacionado con la selección de la base de datos.
- **TABLE:** Utilizado para definir o manipular tablas en la base de datos.
- **ALTER:** Para realizar modificaciones en la estructura de la base de datos.
- **DROP:** Elimina objetos de la base de datos.
- **COLUMN:** Manipula columnas de las tablas.
- **TRUNCATE:** Elimina todos los registros de una tabla, pero mantiene su estructura.
- **USAR:** Indica la base de datos que se utilizará en una sesión.
Mis disculpas por ese descuido. Aquí están los tokens que mencionaste:

- **SELECT:** Utilizado para seleccionar datos de una tabla.
- **FROM:** Indica la tabla desde la cual seleccionar datos.
- **WHERE:** Condición para filtrar los resultados.
- **UPDATE:** Actualiza registros en una tabla.
- **INSERT:** Inserta nuevos registros en una tabla.
- **DELETE:** Elimina registros de una tabla.
- **CONCATENA:** Realiza la concatenación de cadenas.
- **SUBSTRAER:** Obtiene una subcadena de otra cadena.
- **HOY:** Representa la fecha actual.
- **CONTAR:** Se utiliza para contar registros o resultados.
- **SUMA:** Realiza la suma de valores.
- **CAS:** Realiza una evaluación de casos.
- **NULL:** Representa un valor nulo.
- **PRIMARY:** Define una clave primaria en una tabla.
- **FOREING:** Define una clave foránea en una tabla.
- **KEY:** Clave.
- **REFERENCE:** Referencia.
- **PROCEDURE:** Define un procedimiento almacenado.
- **AS:** Se utiliza para definir alias o indicar el inicio de la implementación de un procedimiento o función.
- **EXEC:** Ejecuta un procedimiento almacenado o una consulta SQL dinámica.
- **FUNCTION:** Define una función.
- **IF:** Condición "si" en estructuras de control.
- **WHILE:** Bucle while.
- **THEN:** Parte de la estructura de control "if".
- **ELSE:** Parte de la estructura de control "if" para la condición falsa.
- **ELSEIF:** Parte de la estructura de control "if" para condiciones adicionales.
- **RETURN:** Devuelve un valor de una función o procedimiento.
- **RETURNS:** Especifica el tipo de dato que devuelve una función o procedimiento.
- **BEGIN:** Inicio de un bloque de código.
- **CASE:** Se utiliza en la estructura de control "case".
- **WHEN:** Condición en la estructura de control "case".
- **END:** Fin de un bloque de código.
- **ADD:** Agrega columnas a una tabla.
- **DECLARE:** Declara una variable.
- **SET:** Establece el valor de una variable.
- **VARCHAR:** Tipo de dato para almacenar cadenas de longitud variable.
- **NCHAR:** Tipo de dato para almacenar caracteres de longitud fija.
- **NVARCHAR:** Tipo de dato para almacenar cadenas de longitud variable de caracteres Unicode.
- **R_INT:** Tipo de dato para almacenar números enteros.
- **R_BIT:** Tipo de dato para almacenar valores binarios (bits).
- **R_DECIMAL:** Tipo de dato para almacenar números decimales.
- **DATETIME:** Tipo de dato para almacenar fecha y hora.
- **DATE:** Tipo de dato para almacenar solo la fecha.
- **FOREIGN:** Palabra clave para definir una clave foránea.
- **INTO:** Utilizado en instrucciones como INSERT INTO.
- **VALUES:** Indica los valores que se van a insertar en una tabla.
- **SQL_AND:** Operador lógico AND.
- **SQL_OR:** Operador lógico OR.
- **SQL_NOT:** Operador lógico NOT.

### Expresiones Regulares de Tokens:

¡Entendido! Aquí están las expresiones regulares con sus descripciones sin el prefijo `t_` y encerradas en inline code:

- **`POR`:** Multiplicación (*)
  - Expresión Regular: `r'\*'`

- **`MAS`:** Suma (+)
  - Expresión Regular: `r'\+'`

- **`DIVISION`:** División (/)
  - Expresión Regular: `r'\/'`

- **`MENOS`:** Resta (-)
  - Expresión Regular: `r'\-'`

- **`ASIGNACION`:** Asignación (=)
  - Expresión Regular: `r'\='`

- **`COMPARACION`:** Igualdad (==)
  - Expresión Regular: `r'\=\='`

- **`DISTINTO`:** Desigualdad (!=)
  - Expresión Regular: `r'\!\='`

- **`PUNTO`:** Punto (.)
  - Expresión Regular: `r'\.'`

- **`COMA`:** Coma (,)
  - Expresión Regular: `r'\,'`

- **`PUNTO_Y_COMA`:** Punto y coma ( ; )
  - Expresión Regular: `r'\;'`

- **`DOS_PUNTOS`:** Dos puntos ( : )
  - Expresión Regular: `r'\:'`

- **`MENOR_QUE`:** Menor que (<)
  - Expresión Regular: `r'\<'`

- **`MAYOR_QUE`:** Mayor que (>)
  - Expresión Regular: `r'\>'`

- **`MENOR_O_IGUAL_QUE`:** Menor o igual que (<=)
  - Expresión Regular: `r'\<\='`

- **`MAYOR_O_IGUAL_QUE`:** Mayor o igual que (>=)
  - Expresión Regular: `r'\>\='`

- **`PARENTESIS_IZQ`:** Paréntesis izquierdo (()
  - Expresión Regular: `r'\('`

- **`PARENTESIS_DER`:** Paréntesis derecho ())
  - Expresión Regular: `r'\)'`

- **`LLAVE_IZQ`:** Llave izquierda ({)
  - Expresión Regular: `r'\{'`

- **`LLAVE_DER`:** Llave derecha (})
  - Expresión Regular: `r'\}'`

- **`OR`:** Operador lógico OR (||)
  - Expresión Regular: `r'\|\|'`

- **`AND`:** Operador lógico AND (&&)
  - Expresión Regular: `r'\&\&'`

- **`NOT`:** Operador lógico NOT (!)
  - Expresión Regular: `r'\!'`

- **`NEGACION`:** Negación (!)
  - Expresión Regular: `r'\!'`

- **`CORCHETE_IZQ`:** Corchete izquierdo ([)
  - Expresión Regular: `r'\['`

- **`CORCHETE_DER`:** Corchete derecho (])
  - Expresión Regular: `r'\]'`

- **`ARROBA`:** Símbolo '@'
  - Expresión Regular: `r'\@'`

- **`COMILLASIMPLE`:** Comilla simple (')
  - Expresión Regular: `r"\'"`

- **`comment`:** Comentarios de línea (--)
  - Descripción: Reconoce comentarios de línea que comienzan con "--".
  - Expresión Regular: `r'\-\-.*'`

- **`ID`:** Identificador normal
  - Descripción: Reconoce identificadores que comienzan con una letra o guion bajo, seguidos opcionalmente por letras, números o guiones bajos.
  - Expresión Regular: `r'[a-zA-Z_][a-zA-Z_0-9]*'`

- **`ID_DECLARE`:** Identificador para declaración
  - Descripción: Reconoce identificadores que comienzan con '@', seguidos por letras, números o guiones bajos.
  - Expresión Regular: `r'@[a-zA-Z_][a-zA-Z_0-9]*'`

- **`DATETIMEPRIM`:** Fecha y hora en formato primario
  - Descripción: Reconoce fechas y horas en formato primario dentro de comillas simples.
  - Expresión Regular: `r'\'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\'`

- **`DATEPRIM`:** Fecha en formato primario
  - Descripción: Reconoce fechas en formato primario dentro de comillas simples.
  - Expresión Regular: `r'\'\d{4}-\d{2}-\d{2}\'`

- **`DECIMAL`:** Números decimales
  - Descripción: Reconoce números decimales.
  - Expresión Regular: `r'\d+\.\d+'`

- **`ENTERO`:** Números enteros
  - Descripción: Reconoce números enteros.
  - Expresión Regular: `r'\d+'`

- **`BITPRIM`:** Bits en formato primario (1, 0, null)
  - Descripción: Reconoce bits en formato primario (1, 0 o null).
  - Expresión Regular: `r'1|0|null'`

- **`Nueva linea`:** Nueva línea
  - Descripción: Reconoce una o más secuencias de nueva línea.
  - Expresión Regular: `r'\n+'`

- **`STR`:** Cadenas de texto
  - Descripción: Reconoce cadenas de texto dentro de comillas dobles, con la capacidad de manejar secuencias de escape.
  - Expresión Regular: `r'\"[\s\S]*?\"'`

## Símbolos
### Terminales de DDL y DML

- `p_init`: Representa el punto de inicio de tu gramática, donde se inicializa un programa con una lista de instrucciones.

- `p_instruccionesListado`: Se utiliza para construir una lista de instrucciones, donde cada instrucción puede ser agregada a la lista.

- `p_instruccionSimple`: Maneja el caso en el que solo hay una instrucción, creando una lista que contiene esa instrucción.

- `p_instruccionGeneral`: Define varias instrucciones generales, como la creación de bases de datos, tablas, funciones, procedimientos almacenados, llamadas a procedimientos, etc.

- `p_usarDB`: Representa la instrucción para cambiar la base de datos actual.

- `p_crearBaseDatos`: Define la creación de una nueva base de datos.

- `p_crearTabla`: Maneja la creación de tablas, incluidas las definiciones de columnas.

- `p_tablasEspecifico`, `p_tablasEspecifico2`, `p_columnaDefinicion`: Definen la estructura específica de las tablas y las columnas.

- `p_tipo_datoX`: Definen los diferentes tipos de datos que pueden ser utilizados en las columnas de las tablas.

- `p_nulidad_parametroX`: Define si una columna puede o no ser nula.

- `p_restriccion_parametroX`: Maneja las restricciones de las columnas, como claves primarias, foráneas, etc.

- `p_alterTable`: Se utiliza para realizar operaciones ALTER en tablas, como agregar o eliminar columnas.

- `p_opcionesAlterX`: Define diferentes operaciones ALTER en tablas.

- `p_dropX`: Define las instrucciones para eliminar bases de datos y tablas.

- `p_truncateX`: Define las instrucciones TRUNCATE para bases de datos y tablas.

- `p_dml`: Se encarga de las operaciones DML (Data Manipulation Language) como SELECT, UPDATE, INSERT, DELETE.

- `p_selectX`: Define la operación SELECT y sus componentes.

- `p_from_table_optX`: Define la cláusula FROM de la operación SELECT.

- `p_condition_optX`: Define la cláusula WHERE de la operación SELECT.

- `p_select_listX`: Define la lista de elementos seleccionados en la operación SELECT.

- `p_select_sublistX`: Define sublistas de elementos seleccionados en la operación SELECT.

- `p_select_itemX`: Define elementos individuales seleccionados en la operación SELECT.

- `p_updateX`: Define la operación UPDATE y sus componentes, como la tabla a actualizar y las columnas a modificar.

- `p_set_clausesX`: Define las cláusulas SET en la operación UPDATE.

- `p_insertX`: Define la operación INSERT y sus componentes, como la tabla de destino y los valores a insertar.

- `p_insert_listX`: Define la lista de valores a insertar en la operación INSERT.

- `p_insert_itemX`: Define elementos individuales en la lista de valores de la operación INSERT.

- `p_deleteX`: Define la operación DELETE y sus componentes, como la tabla de la que se eliminarán los datos y la condición para la eliminación.

- `p_delete_tableX`: Define la tabla de la que se eliminarán los datos en la operación DELETE.

- `p_drop_objectX`: Define el objeto (base de datos o tabla) que se eliminará en las instrucciones DROP.

- `p_truncate_tableX`: Define la tabla que se truncará en la instrucción TRUNCATE.

- `p_functionX`: Define una función, especificando su nombre, parámetros y cuerpo.

- `p_procedureX`: Define un procedimiento almacenado, especificando su nombre, parámetros y cuerpo.

- `p_procedure_blockX`: Define el bloque de código dentro de un procedimiento almacenado.

- `p_call_procedureX`: Define la instrucción para llamar a un procedimiento almacenado.

- `p_create_indexX`: Define la operación CREATE INDEX y sus componentes, como el nombre del índice y la tabla a indexar.

- `p_columnasIndexX`: Define las columnas que formarán parte del índice.

- `p_unique_optX`: Define la opción UNIQUE en la operación CREATE INDEX.


### Terminales de SSL

1. `p_funcion_usuario`: Define una función de usuario con parámetros y un tipo de retorno.

2. `p_funcion_usuario2`: Define una función de usuario sin parámetros y con un tipo de retorno.

3. `p_alter_funcion_usuario`: Realiza una alteración en una función de usuario con parámetros y un tipo de retorno.

4. `p_alter_funcion_usuario2`: Realiza una alteración en una función de usuario sin parámetros y con un tipo de retorno.

5. `p_parametros_funcion`: Define parámetros para una función.

6. `p_parametros_funcion2`: Define un solo parámetro para una función.

7. `p_parametro_funcion`: Define un parámetro de función con un identificador y un tipo de dato.

8. `p_parametro_funcion2`: Define un parámetro de función con un identificador y un tipo de dato.

9. `p_tipo_dato_parametro`: Define el tipo de dato de un parámetro.

10. `p_tipo_dato_funcion`: Define el tipo de dato de una función.

11. `p_tipo_dato_variable_funcion`: Define el tipo de dato de una variable en una función.

12. `p_sentencias_funciones`: Define varias sentencias dentro de una función.

13. `p_sentencias_funciones1`: Define una sola sentencia dentro de una función.

14. `p_sentencia_funcion`: Define diferentes tipos de sentencias dentro de una función, como declaraciones de variables, asignaciones, retornos, estructuras condicionales y bucles.

15. `p_declaracion_variables`: Realiza la declaración de varias variables.

16. `p_lista_declaracion_variables`: Define una lista de declaraciones de variables.

17. `p_lista_declaracion_variables2`: Define una sola declaración de variable.

18. `p_declaracion_variable`: Define la declaración de una variable con un identificador y un tipo de dato.

19. `p_set_variable_funcion`: Realiza una asignación a una variable en una función.

20. `p_asignacion_set`: Define una asignación a una variable en una función, ya sea mediante una expresión o una llamada a función.

21. `p_return`: Define una sentencia de retorno en una función.

22. `p_llamada_funcion`: Realiza una llamada a una función.

23. `p_llamada_funcion2`: Realiza una llamada a una función sin parámetros.

24. `p_parametros_llamada_funcion`: Define los parámetros para la llamada a una función.

25. `p_parametros_llamada_funcion2`: Define un solo parámetro para la llamada a una función.

26. `p_parametro_llamada_funcion`: Define un parámetro para la llamada a una función.

27. `p_crear_procedure`: Crea un procedimiento con parámetros.

28. `p_procedure2`: Crea un procedimiento sin parámetros.

29. `p_sentencias_procedimientos`: Define varias sentencias dentro de un procedimiento.

30. `p_sentencias_procedimientos1`: Define una sola sentencia dentro de un procedimiento.

31. `p_sentencia_procedimiento`: Define diferentes tipos de sentencias dentro de un procedimiento, como declaraciones de variables, asignaciones, estructuras condicionales y bucles, así como instrucciones DML y alteraciones de tablas.

32. `p_alter_procedure`: Realiza una alteración en un procedimiento con parámetros.

33. `p_alter_procedure2`: Realiza una alteración en un procedimiento sin parámetros.

34. `p_parametros_procedure`: Define los parámetros para un procedimiento.

35. `p_parametros_procedure2`: Define un solo parámetro para un procedimiento.

36. `p_parametro_procedure`: Define un parámetro para un procedimiento con un identificador y un tipo de dato.

37. `p_parametro_procedure2`: Define un parámetro para un procedimiento con un identificador y un tipo de dato.

38. `p_llamada_procedure`: Realiza una llamada a un procedimiento.

39. `p_llamada_procedure2`: Realiza una llamada a un procedimiento sin parámetros.

40. `p_llamada_procedure3`: Realiza una llamada a un procedimiento con asignaciones.

41. `p_asignaciones_procedure`: Define asignaciones para un procedimiento.

42. `p_asignaciones_procedure2`: Define una sola asignación para un procedimiento.

43. `p_asignacion_procedure`: Define una asignación para un procedimiento con un identificador y una expresión.

44. `p_expresion_if`: Define una estructura condicional `if`.

45. `p_expresion_if2`: Define una estructura condicional `if` con una rama `else`.

46. `p_expresion_if3`: Define una estructura condicional `if` con varias ramas `else if` y una rama `else`.

47. `p_expresion_if4`: Define una estructura condicional `if` con varias ramas `else if`.

48. `p_cuerpo_if_else`: Define el cuerpo de un bloque `if` o `else`.

49. `p_expresion_else`: Define la rama `else` de una estructura condicional.

50. `p_lista_else_if`: Define una lista de ramas `else if` en una estructura condicional.

51. `p_lista_else_if2`: Define una sola rama `else if` en una estructura condicional.

52. `p_expresion_else_if`: Define una rama `else if` en una estructura condicional.

53. `p_expresion_case`: Define una estructura `case` con cláusulas `when` y una rama `else`.

54. `p_expresion_case2`: Define una estructura `case` con cláusulas `when` y sin rama `else`.

55. `p_when_clauses`: Define cláusulas `when` para una estructura `case`.

56. `p_when_clauses2`: Define una sola cláusula `when` para una estructura `case`.

57. `p_while`: Define una estructura de bucle `while`.

## Gramática BNF

### Inicialización
- `init` : `instrucciones`

### Instrucciones
- `instrucciones` : `instrucciones` `instruccion`
                 | `instruccion` 

### Instrucción
- `instruccion` : `crearBaseDatos` `PUNTO_Y_COMA`
               | `crearTabla` `PUNTO_Y_COMA`
               | `crear_funcion_usuario` `PUNTO_Y_COMA`
               | `alter_funcion_usuario` `PUNTO_Y_COMA`
               | `crear_procedure` `PUNTO_Y_COMA`
               | `llamada_procedure` `PUNTO_Y_COMA`
               | `alter_procedure` `PUNTO_Y_COMA`
               | `opcionTruncate` `PUNTO_Y_COMA`
               | `opcionDrop` `PUNTO_Y_COMA`
               | `alterTable` `PUNTO_Y_COMA`
               | `usarDB` `PUNTO_Y_COMA`
               | `dml` `PUNTO_Y_COMA`

### Uso de Base de Datos
- `usarDB` :  `USAR` `ID`

### Creación de Base de Datos
- `crearBaseDatos` : `CREATE` `DATA` `BASE` `ID`

### Creación de Tabla
- `crearTabla` : `CREATE` `TABLE` `ID` `PARENTESIS_IZQ` `tablasEspecifico` `PARENTESIS_DER`

### Especificación de Tablas
- `tablasEspecifico` : `tablasEspecifico` `COMA` `columnaDefinicion`
                   | `columnaDefinicion`

### Definición de Columna
- `columnaDefinicion` : `ID` `tipo_dato` `nulidad_parametro` `restriccion_parametro`

### Tipo de Dato
- `tipo_dato` : `R_INT`
             | `R_DECIMAL`
             | `R_BIT`
             | `DATETIME`
             | `DATE`
             | `NVARCHAR` `PARENTESIS_IZQ` `expresion` `PARENTESIS_DER`
             | `NCHAR` `PARENTESIS_IZQ` `expresion` `PARENTESIS_DER`

### Nulidad del Parámetro
- `nulidad_parametro` : `NULL`
                   | `SQL_NOT NULL`
                   | 

### Restricción del Parámetro
- `restriccion_parametro` : `PRIMARY KEY` `restriccion_parametro`
                      | `PRIMARY KEY`
                      | `REFERENCE` `ID` `PARENTESIS_IZQ` `ID` `PARENTESIS_DER`
                      | 

### Alteración de Tabla
- `alterTable` : `ALTER` `TABLE` `ID` `opcionAlter`

### Opción de Alteración
- `opcionAlter` : `ADD` `COLUMN` `ID` `tipo_dato`
               | `DROP` `COLUMN` `ID`

### Opción de Eliminación
- `opcionDrop` : `DROP` `DATA` `BASE` `ID`
              | `DROP` `TABLE` `ID`

### Opción Truncate
- `opcionTruncate` : `TRUNCATE` `ID`
                  | `TRUNCATE` `TABLE` `ID`

### DML (Data Manipulation Language)
- `dml` : `select`
        | `update`
        | `insert`
        | `delete`

### SELECT
- `select` : `SELECT` `select_list` `from_table_opt`

### Lista de Selección
- `select_list` : `POR`
               | `select_sublist`

### Sublista de Selección
- `select_sublist` : `select_sublist` `COMA` `select_item`
                  | `select_item`

### Elemento de Selección
- `select_item` : `sql_expression` `id_opt`

### Opción ID
- `id_opt` : `ID`
           | 

### Funciones del Sistema
- `funciones_sistema` : `CONCATENA` `PARENTESIS_IZQ` `concat_list_params` `PARENTESIS_DER`
                     | `SUBSTRAER` `PARENTESIS_IZQ` `sql_expression` `COMA` `ENTERO` `COMA` `ENTERO` `PARENTESIS_DER`
                     | `HOY` `PARENTESIS_IZQ` `PARENTESIS_DER`
                     | `CONTAR` `PARENTESIS_IZQ` `POR` `PARENTESIS_DER`
                     | `SUMA` `PARENTESIS_IZQ` `param_suma` `PARENTESIS_DER`
                     | `CAS` `PARENTESIS_IZQ` `cas_value` `AS` `valor` `PARENTESIS_DER`

### Valor para CAS
- `cas_value` : `sql_expression`

### Tipo de Valor
- `valor` : `VARCHAR`
         | `NCHAR`
         | `NVARCHAR`
         | `R_INT`
         | `R_BIT`
         | `R_DECIMAL`
         | `DATETIME`
         | `DATE`

### Tabla
- `table` : `table` `COMA` `ID`
         | `ID`

### UPDATE
- `update` : `UPDATE` `ID` `SET` `assign_list` `WHERE` `sql_expression`

### Lista de Asignación
- `assign_list` : `assign`
              | `assign_list` `COMA` `assign`

### Asignación
- `assign` : `ID` `ASIGNACION` `sql_expression`

### INSERT
- `insert` : `INSERT INTO` `ID` `PARENTESIS_IZQ` `column_list` `PARENTESIS_DER` `VALUES` `PARENTESIS_IZQ` `value_list` `PARENTESIS_DER`

### Lista de Columnas
- `column_list` : `column_list` `COMA` `ID`
               | `ID`

### Lista de Valores
- `value_list` : `value_list` `COMA` `value`
              | `value`

### Valor
- `value` : `STR`
         | `DECIMAL`
         | `ENTERO`
         | `DATEPRIM`
         | `DATETIMEPRIM`

### DELETE
- `delete` : `DELETE FROM` `ID` `WHERE` `sql_expression`


### SELECT
- `select` : `SELECT` `select_list` `from_table_opt`

### Lista de Selección
- `select_list` : `POR`
               | `select_sublist`

### Sublista de Selección
- `select_sublist` : `select_sublist` `COMA` `select_item`
                  | `select_item`

### Elemento de Selección
- `select_item` : `sql_expression` `id_opt`

### Opción ID
- `id_opt` : `ID`
           | 

### Funciones del Sistema
- `funciones_sistema` : `CONCATENA` `PARENTESIS_IZQ` `concat_list_params` `PARENTESIS_DER`
                     | `SUBSTRAER` `PARENTESIS_IZQ` `sql_expression` `COMA` `ENTERO` `COMA` `ENTERO` `PARENTESIS_DER`
                     | `HOY` `PARENTESIS_IZQ` `PARENTESIS_DER`
                     | `CONTAR` `PARENTESIS_IZQ` `POR` `PARENTESIS_DER`
                     | `SUMA` `PARENTESIS_IZQ` `param_suma` `PARENTESIS_DER`
                     | `CAS` `PARENTESIS_IZQ` `cas_value` `AS` `valor` `PARENTESIS_DER`

### Valor para CAS
- `cas_value` : `sql_expression`

### Tipo de Valor
- `valor` : `VARCHAR`
         | `NCHAR`
         | `NVARCHAR`
         | `R_INT`
         | `R_BIT`
         | `R_DECIMAL`
         | `DATETIME`
         | `DATE`

### Tabla
- `table` : `table` `COMA` `ID`
         | `ID`

### UPDATE
- `update` : `UPDATE` `ID` `SET` `assign_list` `WHERE` `sql_expression`

### Lista de Asignación
- `assign_list` : `assign`
              | `assign_list` `COMA` `assign`

### Asignación
- `assign` : `ID` `ASIGNACION` `sql_expression`

### INSERT
- `insert` : `INSERT INTO` `ID` `PARENTESIS_IZQ` `column_list` `PARENTESIS_DER` `VALUES` `PARENTESIS_IZQ` `value_list` `PARENTESIS_DER`

### Lista de Columnas
- `column_list` : `column_list` `COMA` `ID`
               | `ID`

### Lista de Valores
- `value_list` : `value_list` `COMA` `value`
              | `value`

### Valor
- `value` : `STR`
         | `DECIMAL`
         | `ENTERO`
         | `DATEPRIM`
         | `DATETIMEPRIM`

### DELETE
- `delete` : `DELETE FROM` `ID` `WHERE` `sql_expression`
