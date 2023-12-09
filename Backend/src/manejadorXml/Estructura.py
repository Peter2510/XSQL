from ..manejadorXml import obtener
Databases = []


def load():
    global Databases
    ## llamarlo como desde la clase que necesitamos
    Databases = obtener.importAllXMLsInDirectory("./src/data/xml/")
    print(type(Databases))
    print(Databases)
    


def createDatabase(name):
    try:
        database = {}
        database["name"] = name
        database["tables"] = []
        for nombre in Databases:
            if (nombre["name"] == name):
                return 2
        Databases.append(database)
        obtener.exportDataToXML( {
            'tabla1': {"producto": "nuevo", "precio": 1},
            'tabla2': {"producto": "simon", "precio": 3}
        }      , name)
        return 0
    except:
        return 1


# Exportar a XML
data_to_export = {
    'tabla1': {"producto": "nuevo", "precio": 1},
    'tabla2': {"producto": "simon", "precio": 3}
}

#Obtener.exportDataToXML(data_to_export, "simoon2")

# Importar desde XML
#data_imported = obtener.importFileFromXML("nuevo")
#print(data_imported)  # Esto imprimirá el diccionario importado desde el archivo XML


#directory_to_import = "../data/xml/"
#imported_data = obtener.importAllXMLsInDirectory(directory_to_import)
#print(imported_data)

load();

createDatabase("primera")
print(Databases)
for i in Databases:
    print(i["name"])
    for j in i["tables"]:
        print(j["data"]['producto'])