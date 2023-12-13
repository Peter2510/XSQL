import xml.etree.ElementTree as ET
import pandas as pd

# Tu XML
xml_data = '''<?xml version="1.0" encoding="UTF-8"?>
<libros>
    <libro>
        <titulo>El señor de los anillos</titulo>
        <autor>J.R.R. Tolkien</autor>
        <anio>1954</anio>
    </libro>
    <libro>
        <titulo>Cien años de soledad</titulo>
        <autor>Gabriel García Márquez</autor>
        <anio>1967</anio>
    </libro>
    <libro>
        <titulo>1984</titulo>
        <autor>George Orwell</autor>
        <anio>1949</anio>
    </libro>
</libros>
'''

# Parsear el XML
root = ET.fromstring(xml_data)

# Crear un diccionario para almacenar los datos
data_dict = {'titulo': [], 'autor': []}

# Iterar sobre los elementos 'persona'
for persona_elem in root.findall('.//libro'):
    data_dict['titulo'].append(persona_elem.find('titulo').text)
    data_dict['autor'].append(persona_elem.find('autor').text)
    

# Crear un DataFrame con pandas
df = pd.DataFrame(data_dict)

# Mostrar el DataFrame
print(df)