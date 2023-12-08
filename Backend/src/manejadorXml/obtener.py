import xml.etree.ElementTree as ET
def exportFileToXML(struct, name):
    try:
        root = ET.Element("Data")
        tree = ET.ElementTree(root)
        
        for key, value in struct.items():
            element = ET.SubElement(root, key)
            element.text = str(value)
        
        tree.write(f".data/xml/{name}.xml", encoding="utf-8", xml_declaration=True)
        print(f"Datos exportados a {name}.xml exitosamente.")
    except Exception as e:
        print(f"Error al exportar datos a XML: {str(e)}")

def importFileFromXML(name):
    try:
        tree = ET.parse(f".data/xml/{name}.xml")
        root = tree.getroot()
        
        data = {}
        for child in root:
            data[child.tag] = child.text
        
        print(f"Datos importados desde {name}.xml exitosamente.")
        return data
    except Exception as e:
        print(f"Error al importar datos desde XML: {str(e)}")
        return {}
