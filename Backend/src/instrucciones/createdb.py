from ..abstract.abstractas import Abstract
from ..manejadorXml import manejo 

class createDB(Abstract):
    
    def __init__(self, fila, columna, nombre):
        self.nombre = nombre
        super().__init__(fila, columna)

    def interpretar(self,environment):
        nombre = self.nombre

        if not isinstance(nombre,str):
            return {'Error': 'El nombre indicado de la base de datos no es una cadena.', 'Fila':self.fila, 'Columna': self.columna }
        resultado = manejo.createDatabase(nombre)
        if (resultado == 0):
            #Se creo la base de datos correctamente.
           # environment.createDataBase(nombre)#Guardamos la metadata en el entorno global.
            return 'La base de datos ' + self.nombre + ' ha sido creada.' 
        elif resultado == 1:
            #Error al crear
            return {'Error':'Ocurrió un error. La base de datos' + nombre + ' no pudo ser creada.', 'Fila':self.fila, 'Columna':self.columna}
        elif resultado == 2:
            #Ya creada
            return {'Error': "La base de datos " + nombre + " ya existe.", 'Fila': self.fila, 'Columna': self.columna}
        else:
            return {'Error': "Error en el almacenamiento.", 'Fila': self.fila, 'Columna': self.columna}
