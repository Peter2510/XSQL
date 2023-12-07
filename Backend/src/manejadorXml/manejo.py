import os 
import json
import xml.etree.ElementTree as ET


path = 'src/data/json/'
dataPath = path + 'databases'
xml_path = 'src/data/xml/'

def initCheck():
    if not os.path.exists('src/data'):
        os.makedirs('src/data')
    if not os.path.exists('src/data/json'):
        os.makedirs('src/data/json')
    if not os.path.exists('src/data/json/databases'):
        data = {}
        with open('src/data/json/databases', 'w') as file:
            json.dump(data, file)
    if not os.path.exists('src/data/xml'):
       os.makedirs('src/data/xml')


def read(path: str) -> dict:
    with open(path) as file:
        return json.load(file)    
    
def write(path: str, data: dict):
    with open(path, 'w') as file:
        json.dump(data, file)

def createDatabase(database: str) -> int:

    try:
        if not database.isidentifier():
            raise Exception()
        initCheck()
        data = read(dataPath)
        print("path:",dataPath)

        if database in data:
            return 2
        print(database)
        new = {database: {}}
        data.update(new)
        write(dataPath, data)
        return 0
    except:
        return 1
# UPDATE a register
def update(database: str, table: str, register: dict, columns: list) -> int:
    initCheck()
    dump = False
    hide = False
    ncol = None
    pkey = None
    pk = ""
    with open('src/data/json/databases') as file:
        data = json.load(file)
        if not database in data:
            return 2
        else: 
            if table not in data[database]:
                return 3
            if "PKEY" not in data[database][table]:
                # hidden pk
                hide = True
            else:
                # defined pk
                pkey = data[database][table]["PKEY"]            
    with open('src/data/json/'+database+'-'+table) as file:
        data = json.load(file)
        if hide:
            pk = columns[0]
        else:
            for i in pkey:
                pk += str(columns[i])
        if not pk in data:
            return 4
        else:            
            for key in register:
                data[pk][key] = register[key]
        dump = True
    if dump:
        with open('src/data/json/'+database+'-'+table, 'w') as file:
            json.dump(data, file)
        return 0
    else:
        return 1

def createTable(database: str, table: str, columns_info: dict) -> int:
    try:
        if not database.isidentifier() or not table.isidentifier() or not isinstance(columns_info, dict):
            raise Exception()

        initCheck()
        data = read(dataPath)
        if not database in data:
            return 2        
        if table in data[database]:
            return 3
        
        # Agregar la nueva tabla a la base de datos
        new_table_info = {"NCOL": len(columns_info)}
        
        # Aquí se podría añadir la lógica para agregar las columnas
        for column_name, column_info in columns_info.items():
            # Verificar si la tabla ya existe en la base de datos
            if table not in data[database]:
                # Si no existe, creamos una nueva tabla con las columnas proporcionadas
                data[database][table] = {column_name: column_info}
            else:
                # Si la tabla ya existe, actualizamos su información de columnas
                data[database][table][column_name] = column_info

        # Guardamos los cambios en la base de datos
        write(dataPath, data)
        
        
        # Crear el archivo correspondiente para la tabla (si es necesario)
        dataTable = {}
        write(path + database + '-' + table, dataTable)
        
        return 0
    except:
        return 1



def convert_to_xml(database_name):
    try:
        data = read(dataPath)
        if database_name not in data:
            raise ValueError("La base de datos especificada no existe.")
        
        root = ET.Element("Database")
        for table_name, table_data in data[database_name].items():
            table = ET.SubElement(root, "Table")
            table.set("name", table_name)
            
            if table_data:
                columns = ET.SubElement(table, "Columns")
                for column_name, column_info in table_data.items():
                    column = ET.SubElement(columns, "Column")
                    column.set("name", column_name)
                    column.set("info", column_info)
        
        xml_tree = ET.ElementTree(root)
        xml_tree.write(f"data/xml/{database_name}.xml", encoding="utf-8", xml_declaration=True)
        
        print(f"La base de datos '{database_name}' se ha convertido a XML correctamente.")
    except Exception as e:
        print(f"Error al convertir la base de datos a XML: {str(e)}")






def prueba():
    nombre_bd = "sss3"
    nombre_tabla = "prueba"
    columnas = {
        "producto": "int not null",
        "area": "varchar(100) not null"
    }
    resultado2 = createDatabase(nombre_bd);
prueba();
#resultado = createTable(nombre_bd, nombre_tabla, columnas)

#if resultado == 0:
#    print(f"La tabla '{nombre_tabla}' se creó exitosamente en '{nombre_bd}'.")
#elif resultado == 1:
#    print("Error al intentar crear la tabla.")
# ... Resto del manejo de resultados
# Llamamos a la función para convertir la base de datos especificada a XML
#convert_to_xml("prueba")