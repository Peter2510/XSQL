import xml.etree.ElementTree as ET
import json
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
        file_path = f"./src/data/xml/{name}.xml"
        if os.path.exists(file_path):
            tree = ET.parse(file_path)
            root = tree.getroot()
        else:
            root = ET.Element("Database")
            root.set("name", name)
        print(type(data), "<<<<<<<<<<,")

        if (data != {}):
            table = ET.SubElement(root, "Table")
            table.set("name", data['name'])

            ## ingreso de la otra etiqueta 
            info = ET.SubElement(table, "Estructura")
            for entry in data['data']:

                principal = ET.SubElement(info, "Principal")
                principal.set("name", entry['nombre'])

                data_element = ET.SubElement(principal, "Atributo1")
                data_element.set("tipo", entry['data']['tipo'])
                data_element.text=("1")

                data_element2 = ET.SubElement(principal, "Atributo2")
                data_element2.set("nulidad", str(entry['data']['nulidad']))
                data_element2.text=("2")


         
                # Si 'restricciones' es un entero
                if isinstance(entry['data']['restricciones'], int):
                    data_element3 = ET.SubElement(principal, "Atributo3")
                    data_element3.set("restricciones", str(entry['data']['restricciones']))
                    data_element3.text = str(entry['data']['restricciones'])  # Aquí asignas el entero

                # Si 'restricciones' es un diccionario
                elif isinstance(entry['data']['restricciones'], dict):
                    # Se crea el elemento Atributo3
                    data_element3 = ET.SubElement(principal, "Atributo3")
                    data_element3.set("restricciones", str(2))

                    # Se desglosa el diccionario y se agregan los subelementos
                    restricciones = entry['data']['restricciones']
                    for key, value in restricciones.items():
                        sub_element = ET.SubElement(data_element3, key)
                        sub_element.text = str(value)




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
        xml_data = []
        for filename in os.listdir(directory):
            if filename.endswith(".xml"):
                file_path = os.path.join(directory, filename)
                tree = ET.parse(file_path)
                root = tree.getroot()

                database_name = root.get("name")
                database_tables = []
                for table in root.findall("Table"):
                    table_name = table.get("name")
                    table_data = {'estructura': {}, 'datos': []}

                    # Obtener la información de la estructura
                    structure_info = table.find("./Estructura")
                    if structure_info is not None:
                        structure_data = {}
                        for principal in structure_info.findall("Principal"):
                            principal_name = principal.get("name")
                            attributes = {}
                            attrib3_info = principal.find("./Atributo3")

                            if attrib3_info is not None:
                                attrib3_data = {}
                                attrib3_data['tipo'] = attrib3_info.attrib
                                for sub_element in attrib3_info.iter():
                                    if sub_element.tag != 'Atributo3':
                                        attrib3_data[sub_element.tag] = sub_element.text
                                attributes['Atributo3'] = attrib3_data
                            else:
                                # No se encontró la etiqueta Atributo3 en este Principal
                                attributes['Atributo3'] = None

                            # Obtener los otros atributos de la estructura
                            for attribute in principal.findall("*"):
                                if attribute.tag != 'Atributo3':
                                    attributes[attribute.tag] = attribute.attrib

                            structure_data[principal_name] = {"nombre": principal_name, "caracteristicas": attributes}
                        table_data['estructura'] = structure_data


                    # Obtener los datos específicos
                    datos_elements = table.findall("./Datos/DatosEspecifico")
                    if datos_elements:
                        for datos in datos_elements:
                            datos_specifico = {}
                            for attribute in datos.findall("*"):
                                datos_specifico[attribute.tag] = attribute.text
                            table_data['datos'].append(datos_specifico)

                    database_tables.append({'name': table_name, 'data': table_data})

                xml_data.append({'name': database_name, 'tables': database_tables})

        return xml_data
    except Exception as e:
        print(f"Error al importar datos desde XML: {str(e)}")
        return []


def import_xml_db(db_name):
    directory = f"./src/data/xml/{db_name}.xml"
    try:
        # Cargar el archivo XML
        tree = ET.parse(directory)
        root = tree.getroot()

        database_name = root.get("name")
        database_tables = []
        for table in root.findall("Table"):
            table_name = table.get("name")
            table_data = {'estructura': {}, 'datos': []}

            # Obtener la información de la estructura
            structure_info = table.find("./Estructura")
            if structure_info is not None:
                structure_data = {}
                for principal in structure_info.findall("Principal"):
                    principal_name = principal.get("name")
                    attributes = {}
                    for attribute in principal.findall("*"):
                        attributes[attribute.tag] = attribute.attrib
                    structure_data[principal_name] = attributes
                table_data['estructura'] = structure_data

            # Obtener los datos específicos
            datos_elements = table.findall("./Datos/DatosEspecifico")
            if datos_elements:
                for datos in datos_elements:
                    datos_specifico = {}
                    for attribute in datos.findall("*"):
                        datos_specifico[attribute.tag] = attribute.text
                    table_data['datos'].append(datos_specifico)

            database_tables.append({'name': table_name, 'data': table_data})

        return {'name': database_name, 'tables': database_tables}

    except FileNotFoundError:
        # print('El archivo "{}" no existe.'.format('tu_archivo.xml'))
        return None
    except Exception:
        return None
