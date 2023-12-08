import obtener
Databases = []
Databases2 = []



def load():
    global Databases2
    Databases2 = obtener.importAllXMLsInDirectory("../data/xml/")
    print(type(Databases2))
    print(Databases2[0])
    print(Databases2)
    


def createDatabase(name):
    database = {}
    database["name"] = name
    database["tables"] = []
    Databases.append(database)
    obtener.exportDataToXML({'tabla1': {"Atributo1A": "aas", "Atributo2A": "sfs"}}, name)


# Exportar a XML
data_to_export = {
    'tabla1': {"Atributo1A": "aas", "Atributo2A": "sfs"},
    'tabla2': {"Atributo1B": "daas", "Atributo2B": "sssfs"}
}

#Obtener.exportDataToXML(data_to_export, "simoon2")

# Importar desde XML
#data_imported = obtener.importFileFromXML("nuevo")
#print(data_imported)  # Esto imprimirá el diccionario importado desde el archivo XML


#directory_to_import = "../data/xml/"
#imported_data = obtener.importAllXMLsInDirectory(directory_to_import)
#print(imported_data)

load();

createDatabase("nuevaDB")