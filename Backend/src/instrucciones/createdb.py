from ..abstract.abstractas import Abstract
from ..manejadorXml import manejo, Estructura 



class createDB(Abstract):
    
    def __init__(self, fila, columna, nombre):
        self.nombre = nombre
        super().__init__(fila, columna)

    def interpretar(self,environment):

        nombre = self.nombre

        if not isinstance(nombre,str):
            environment.addError("Semantico", "" ,f"El nombre indicado de la base de datos no es una cadena", self.fila, self.columna )
            return {'Error': 'El nombre indicado de la base de datos no es una cadena.', 'Fila':self.fila, 'Columna': self.columna }
       
        Estructura.load();
        print("<<",Estructura.Databases)
        resultado  = Estructura.createDatabase(nombre);
        #resultado = manejo.createDatabase(nombre) #CREA EL ARCHIVO
        if (resultado == 0):
            #Se creo la base de datos correctamente.
            #LO GUARDA EN MEMORIA
          #  environment.createDataBase(nombre)#Guardamos la metadata en el entorno global.
            print( 'La base de datos ' + self.nombre + ' ha sido creada.' )
            return { 'La base de datos ' + self.nombre + ' ha sido creada.': f"Columnas alteradas {len(data) - len(data_filtered)}"} 
        elif resultado == 1:
            #Error al crear
            environment.addError("Semantico", {nombre} ,f"Ocurrió un error. La base de datos {nombre} no pudo ser creada", self.fila, self.columna)
            print( 'Ocurrió un error. La base de datos' + nombre + ' no pudo ser creada.' )
            return {'Error':'Ocurrió un error. La base de datos' + nombre + ' no pudo ser creada.', 'Fila':self.fila, 'Columna':self.columna}
        elif resultado == 2:
            #Ya creada
            print ( "La base de datos " + nombre + " ya existe" )
            environment.addError("Semantico", {nombre} ,f"La base de datos { nombre}   ya existe",  self.fila, self.columna)

            return {'Error': "La base de datos " + nombre + " ya existe.", 'Fila': self.fila, 'Columna': self.columna}
        else:
            environment.addError("Semantico", "" ,f"Error en el almacenamiento", self.fila, self.columna)
            print('Error', "Error en el almacenamiento.", 'Fila', self.fila, 'Columna', self.columna)
            return {'Error': "Error en el almacenamiento.", 'Fila': self.fila, 'Columna': self.columna}
            


    def accept(self, visitor, environment):
        visitor.visit(self, environment)
