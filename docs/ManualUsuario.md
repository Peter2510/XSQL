# Manual de Usuario
se puede visualizar un editor de texto en el cual se pueden realizar distintas funcionalidades.
* Crear: En este espacio se puede generar el archivo que desea el usuario
* seleccion de base de datos: el usario debera de ingresar la base de datos que quiere exportar.
* Crear Dump: se podra generar un dump en base a la base de datos ingresada.
* Exportar: el usario podra exportar todos los inserts de la base de datos
* Leer: El usuario podra cargar una base de datos al editor de codigo.
* Guardar Como: El usuario podra guardar el archivo en el que estaba trabajando.
![Alt text](img/image2.png)
Al momento de ejecutar se puede observar que la consola tiene cambios de colores en palabras reservadas y ademas en dado caso de errores, esta cuenta con una consola de salida de mensajes

![Alt text](img/image.png)
Al momento de ejecutar la opcion de 'DeterminarDB', este mostrara en pantalla, un recuadro de texto, donde el usaurio ingresara que base de datos quiere, para exportar.
![Alt text](img/image3.png)
Ya con una base de datos seleccionada, podra utilziar el 'Generar Dump', el cual genera el dump de dicha base de datos
![Alt text](img/image4.png)
![Alt text](img/image-1.png)
Ahora para el export, este boton al momento de ya haber seleccionado la base de dato, generara todos los inserts que tenga en el xml de la base de datos seleccionada:
![Alt text](img/image5.png)
El Leer, hace la funcion de insert, ya que cargara a partir de un archivo con estension sql, toda la informacion al editor de texto.
![Alt text](img/image6.png)
posteriormente, saldra en el apartado de archivos y para cargar, se debera ejecutar leer nuevamente.
![Alt text](img/image7.png)
![Alt text](img/image8.png)
Asi generando de una nueva ventana el archivo, el trabajo se puede generar por distitnas ventanas, para ello esta la opcion de nuevo.
![Alt text](img/image9.png)
El cual mostrara una ventana emergente para poder determinar que nombre de archivo desea
![Alt text](img/image10.png)
Asi generando una nueva ventana del edito de codigo con ese nombre
![Alt text](img/image11.png)
En dado caso, el usuario no quiera la existente ventana, puede pulsat cerrar pestaña, para poder cerrar la ventana en donde se encuentra
![Alt text](img/image12.png)
El usuario se puede mover a traves de las ventanas del editor de codigo
![Alt text](img/image13.png)
Ahora en las opciones de ejecucion, el usuario podra seleccion entre ejecutar y el Ast.
Ejecutar determinara lo que se realice en el edito de texto y mostrara en la ventana de mensajes que es lo que realiza, entre mensajes de ejecucion correcta y errores
![Alt text](img/image14.png)
![Alt text](img/image17.png)
Ademas se puede limpiar todo en consola 
![Alt text](img/image16.png)
Al hacer eso la opcion del AST desaparecera, ya que seria una nueva pruba.
En el caso de una ejecucion correcta, se mostrara en otra ventana del navegador el AST generado con las instrucciones que el usaurio determino.
![Alt text](img/image15.png)