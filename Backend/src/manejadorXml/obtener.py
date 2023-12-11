import xml.etree.ElementTree as ET

import os 

def exportAllXMLsInDirectory(directory):
    try:
        for filename in os.listdir(directory):
            if filename.endswith(".xml"):
                file_path = os.path.join(directory, filename)
                tree = ET.parse(file_path)
                root = tree.getroot()
                
                struct = {}
                for child in root:
                    struct[child.tag] = child.text
                
                exportFileToXML(struct, filename.split(".")[0] + "_exported")
    except Exception as e:
        print(f"Error al exportar datos desde XML: {str(e)}")


def exportDataToXML(data, name):
    try:
        table_name = data['name']
        table_data = data['data']

        root = ET.Element("Database")
        root.set("name", name)

        table = ET.SubElement(root, "Table")
        table.set("name", table_name)

        for key, value in table_data.items():
            element = ET.SubElement(table, key)
            element.text = str(value)

        tree = ET.ElementTree(root)
        tree.write(f"./src/data/xml/{name}.xml", encoding="utf-8", xml_declaration=True)
        print(f"Datos exportados a {name}.xml exitosamente.")
    except Exception as e:
        print(f"Error al exportar datos a XML: {str(e)}")




def importFileFromXML(name):
    try:
        tree = ET.parse(f"{name}.xml")
        root = tree.getroot()
        
        data = {}
        for child in root:
            data[child.tag] = child.text
        
        print(f"Datos importados desde {name}.xml exitosamente.")
        return data
    except Exception as e:
        print(f"Error al importar datos desde XML: {str(e)}")
        return {}


def importAllXMLsInDirectory(directory):
    try:
        xml_data = {}
        for filename in os.listdir(directory):
            if filename.endswith(".xml"):
                file_path = os.path.join(directory, filename)
                tree = ET.parse(file_path)
                root = tree.getroot()

                table_data = {}
                for table in root.findall("Table"):
                    table_name = table.get("name")
                    data = {}
                    for child in table:
                        data[child.tag] = child.text
                    table_data[table_name] = data
                
                xml_data[filename.split(".")[0]] = table_data
                converted_list = [
            {'name': database_name, 'tables': [{'name': table_name, 'data': table_data} for table_name, table_data in tables.items()]} if tables else {'name': database_name, 'tables': []}
            for database_name, tables in xml_data.items()
            ]
        return converted_list
    except Exception as e:
        print(f"Error al importar datos desde XML: {str(e)}")
        return []
    
