from ..manejadorXml import obtener
Databases = []
nombreActual = ""
import json

def load():
    global Databases
    global nombreActual
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
        obtener.exportDataToXML( {} , name, None)
        return 0
    except:
        return 1


# Exportar a XML
data_to_export = {
    'tabla1': {"producto": "nuevo", "precio": 1},
    'tabla2': {"producto": "simon", "precio": 3}
}


##metodo para crear tablas:


##### VER BIEN CON LO DEL EXPORT
def crearTabla(nombreDB, nombreTabla, parametros):
    tabla = {}
    print(type(parametros), "+++++++")
    # Comprobar si parametros es una cadena JSON y convertirla a un diccionario si es necesario
    if isinstance(parametros, list):
        tabla["data"] = []
 
        for parametro in parametros:
            if isinstance(parametro, dict):
                print(parametro,"++++++++++++")
                tabla["data"].append(parametro)


    # para las columnas
    tabla["name"]= nombreTabla
    print(tabla["name"], "bbb")

    # agregar las tablas 
    for bases in Databases:
        if bases["name"] == nombreDB:
            bases["tables"].append(tabla)
            break

    obtener.exportDataToXML(tabla , nombreDB, None)


#Obtener.exportDataToXML(data_to_export, "simoon2")

# Importar desde XML
#data_imported = obtener.importFileFromXML("nuevo")
#print(data_imported)  # Esto imprimirá el diccionario importado desde el archivo XML


#directory_to_import = "../data/xml/"
#imported_data = obtener.importAllXMLsInDirectory(directory_to_import)
#print(imported_data)



