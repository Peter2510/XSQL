from ..manejadorXml import obtener

Databases = []
nombreActual = ""
import json
import xml.etree.ElementTree as ET


### metodo para cargar toda la info 
def load():
    global Databases
    global nombreActual
    ## llamarlo como desde la clase que necesitamos
    Databases = obtener.importAllXMLsInDirectory("./src/data/xml/")
    print(type(Databases))
    #print(Databases)
    


def createDatabase(name):
    try:
        database = {}
        database["name"] = name
        database["tables"] = []
        for nombre in Databases:
            if (nombre["name"] == name):
                return 2
        Databases.append(database)
        obtener.exportDataToXML({}, name)
        return 0
    except:
        return 1


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
                print(parametro, "++++++++++++")
                tabla["data"].append(parametro)

    # para las columnas
    tabla["name"] = nombreTabla
    print(tabla["name"], "bbb")

    # agregar las tablas 
    for bases in Databases:
        if bases["name"] == nombreDB:
            bases["tables"].append(tabla)
            break

    obtener.exportDataToXML(tabla, nombreDB)


def insertTabla(xml_file, table_name, values):
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()

        # Encuentra la tabla deseada
        table = root.find(f"./Table[@name='{table_name}']")
        if table is None:
            print(f"Tabla '{table_name}' no encontrada en el archivo XML.")
            return

        existing_data = table.find("./Datos[@name='nuevo_registro']")
        if existing_data is not None:
            # Crea un nuevo elemento para cada clave y valor proporcionado
            datosEtiqueta = ET.SubElement(existing_data, "DatosEspecifico")
            for key, value in values.items():
                data_element = ET.SubElement(datosEtiqueta, key)
                data_element.text = str(value)
        else:
            # Crea una nueva etiqueta 'Datos' con los valores proporcionados
            principal = ET.SubElement(table, "Datos")
            principal.set("name", "nuevo_registro")
            datosEtiqueta = ET.SubElement(principal, "DatosEspecifico")

            # Agrega los valores proporcionados a los atributos
            for key, value in values.items():
                data_element = ET.SubElement(datosEtiqueta, key)
                data_element.text = str(value)

        # Guarda los cambios en el archivo XML
        tree.write(xml_file, encoding="utf-8", xml_declaration=True)
        print(f"Inserción exitosa en la tabla '{table_name}' del archivo {xml_file}.")
    except Exception as e:
        print(f"Error al insertar datos en el XML: {str(e)}")


## ver lo del truncate
def truncateTable(xmlPath, nombreTabla):
    tree = ET.parse(xmlPath)
    root = tree.getroot()
    for table in root.findall(".//Table[@name='{}']".format(nombreTabla)):
        for valores in table.findall("Datos"):
            table.remove(valores)

    tree.write(xmlPath, encoding="utf-8", xml_declaration=True)


## para que agregue columnas

def alterColumnadd(xmlArchivo, nombreTabla, nombreColumna, tipoColumna):
    tree = ET.parse(xmlArchivo)
    root = tree.getroot()

    for table in root.findall(".//Table[@name='{}']".format(nombreTabla)):
        existing_data = table.find("./Estructura")
        nuevaColumna = ET.SubElement(existing_data,"Principal", name=nombreColumna)
        atributo1=ET.SubElement(nuevaColumna, "Atributo1")
        atributo1.text = tipoColumna
    tree.write(xmlArchivo, encoding="utf-8", xml_declaration=True)


def alterColumnDrop(xmlArchivo, nombreTabla, nombreColumna):
    tree = ET.parse(xmlArchivo)
    root = tree.getroot()

    for table in root.findall(".//Table[@name='{}']".format(nombreTabla)):
        for column in table.findall("./Estructura/Principal[@name='{}']".format(nombreColumna)):
            # Verifica si la columna está presente antes de intentar eliminarla
            if column is not None:
                table.find("./Estructura").remove(column)
                print(f"Columna '{nombreColumna}' eliminada de la tabla '{nombreTabla}'.")
                break  # Rompe el bucle luego de eliminar la columna
    
    tree.write(xmlArchivo, encoding="utf-8", xml_declaration=True)


#Obtener.exportDataToXML(data_to_export, "simoon2")

# Importar desde XML
# data_imported = obtener.importFileFromXML("nuevo")
# print(data_imported)  # Esto imprimirá el diccionario importado desde el archivo XML


# directory_to_import = "../data/xml/"
# imported_data = obtener.importAllXMLsInDirectory(directory_to_import)
# print(imported_data)


def comprobar_tabla_columnas(nombre):
    # print(Databases)
    return True


def get_current_db():
    if nombreActual == "" or nombreActual is None:
        return None

    db = obtener.import_xml_db(nombreActual)

    return db


def comprobar_tablas(tablas: list[str]):
    tables = []
    db = get_current_db()

    if db is None:
        return False, "No está usando una DB"

    for name in tablas:
        tb = next((obj for obj in db.get("tables", []) if obj.get("name", "") == name), None)
        if tb is None:
            return False, f"{nombreActual}.{name} no existe"

        tables.append(tb)

    return True, tables


def filter_by_table_and_name(table_name: str | None, column_name: str):
    def filter_by(table) -> bool:
        tb_name = table.get("name", None)
        if tb_name is None:
            return False

        if table_name is not None and table_name != tb_name:
            return False

        data = table.get("data", None)

        if data is None:
            return False

        estructura = data.get("estructura", None)

        if estructura is None:
            return False

        if column_name in estructura:
            return True

        return False

    return filter_by


def find_tables(tables: list, name: str, table_name: str | None) -> list:
    tables_found = list(filter(filter_by_table_and_name(table_name=table_name, column_name=name), tables))
    return tables_found


def actualizar_datos_en_xml(name, data):
    if nombreActual == "" or nombreActual is None:
        return None

    directory = f"./src/data/xml/{nombreActual}.xml"
    try:
        # Cargar el archivo XML
        tree = ET.parse(directory)
        root = tree.getroot()

        table = root.find(".//Table[@name='{}']".format(name))

        if table is not None:
            datos = table.find('Datos')
            for elemento in datos.findall('DatosEspecifico'):
                datos.remove(elemento)

            for diccionario in data:
                datos_especifico = ET.SubElement(datos, 'DatosEspecifico')
                for key, valor in diccionario.items():
                    elemento = ET.SubElement(datos_especifico, key)
                    elemento.text = valor

            tree.write(directory)
            return True
        else:
            return None

    except FileNotFoundError:
        # print('El archivo "{}" no existe.'.format('tu_archivo.xml'))
        return None
    except Exception:
        return None
