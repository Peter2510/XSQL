from src.manejadorXml import obtener
Databases = []



def load():
    global Databases
    Databases = obtener.importFileFromXML("Databases")


def createDatabase(name):
    database = {}
    database["name"] = name
    database["tables"] = []
    Databases.append(database)
    obtener.exportFileToXML(Databases, "Databases")


# Cargar datos existentes
load()

# Crear una nueva base de datos
createDatabase("NombreDeLaBaseDeDatos")