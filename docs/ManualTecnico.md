#Manual Tecnico

## Detalles del proyecto


![Alt text](img/arq.png)

La elección de la arquitectura cliente-servidor para el desarrollo de la aplicación proporciona una estructura organizada y eficiente. El cliente se desarrollo utilizando Angular, lo que implica una interfaz de usuario dinámica y amigable. Por otro lado, el servidor se implementó mediante Python con Flask, aprovechando la versatilidad y capacidad.

Para los aspectos relacionados con el análisis léxico y sintáctico de la aplicación, se utilizó la librería PLY.


## Cliente

La aplicación Angular se ha organizado cuidadosamente para mejorar la legibilidad, mantenibilidad y escalabilidad del código. La estructura del proyecto sigue las mejores prácticas de Angular y se han definido paquetes específicos para agrupar módulos y componentes relacionados. 

Este enfoque organizado y modular puede facilitar el mantenimiento y la comprensión del código.

A continuación, se presenta la estructura de directorios principal: 

**src/analyze**: Contiene la clase encargada de almacenar un archivo en formato .sql, se almacena tanto el nombre como el contenido para su posterior análisis. 

**app/data-bases**: Contiene el componente que se encarga de mostrar las bases de datos almacenadas y permite ver en una estructura de arbol cada una de las tablas que compone la base de datos.

**app/data-bases/models** Este paquete almacena la lógica necesaria para visualizar las tablas cuando se selecciona una base de datos específica en la estructura de arbol. Este directorio en sí esta dedicado a la manipulación y presentación de datos relacionados con las tablas de la base de datos en el contexto de la aplicación.

**app/editor-manager**: Este componente en cuestion es el encargado de manejar toda la parte de las pestañas junto con su editor de texto correspondiente, la consola de salida, las tablas de simbolos y las tablas de funciones almacenadas en las bases de datos.

**app/obtencion-dbdump**:Este paquete se encarga de gestionar la funcionalidad de dump en la aplicación. Este paquete integra tanto la parte visual como la lógica necesaria para llevar a cabo esta operación.

**app/service** Este direcctorio juega un papel importante en la aplicación al contener la clase encargada de realizar peticiones a la API. Esta clase realiza diversas solicitudes que abarcan distintos aspectos del funcionamiento de la aplicación. A continuación se amplia la informacion: 

1.  **Bases de Datos Almacenadas**: La clase compilacion.service es responsable de realizar peticiones para obtener información sobre las bases de datos almacenadas en la aplicación. 
    
2.  **Compilación**: Se maneja la lógica relacionada con la compilación del código fuente en formato XSQL de la aplicación. 
    
3.  **Manejo de Errores**: La clase en **app/service** se ocupa de las solicitudes relacionadas con la gestión de errores. Incluye la obtención de detalles sobre errores léxicos, sintácticos y semanticos.
    
4.  **Tablas de Símbolos y Funciones**: Se encarga de las solicitudes relacionadas con la obtención de información sobre las tablas de símbolos y funciones generadas durante el análisis del código fuente.
    
5.  **Generación de Código de Tres Direcciones y AST**: Por último, la clase también se encarga de solicitudes para la generación de código de tres direcciones y la representación del Árbol de Sintaxis Abstracta (AST).

**app/tab-header**: Este paquete desempeña un papel específico en la aplicación al encargarse del manejo de la extensión **.sql** para cada pestaña abierta en el editor, junto con la gestión del logo correspondiente. En general es una clase especializada diseñada para mejorar la experiencia de edición de archivos SQL en un entorno de editor. 

**app/text-editor**: Este paquete maneja el marcado de la linea y columna actual dentro del editor, asi como el editor de codigo mismo utilizado, muestra las palabras resaltadas en sintaxis XSQL.