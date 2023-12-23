class DataBaseTmp:
    'Esta clase almacena los procedimientos y funciones de una base de datos'
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.funciones = {}
        self.procedimientos = {}
        
    def existeFuncion(self, nombreFuncion):
        return nombreFuncion in self.funciones

class Environment(list):
       
    def __init__(self, padre=None):
        super().__init__()
        self.databases = []

    def existeFuncion(self, nombreFuncion):
        # Busca la instancia de DataBaseTmp en la lista
        pass
    
    def indexDB(self, nombreDB):
        # Busca la instancia de DataBaseTmp en la lista
        for i, bd in enumerate(self.databases):
            if bd.nombre == nombreDB:
                return i
        return -1
            
    
env = Environment()
db = DataBaseTmp("Prueba1")
db2 = DataBaseTmp("Prueba2")
db3 = DataBaseTmp("Prueba3")
db4 = DataBaseTmp("Prueba4")

env.databases.append(db)
env.databases.append(db2)
env.databases.append(db3)
env.databases.append(db4)

# Verifica si la función "Saludar" existe en la base de datos "Prueba1"
print(env.indexDB("Prueba4"))


