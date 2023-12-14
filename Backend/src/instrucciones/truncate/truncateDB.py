from ...abstract.abstractas import Abstract
import pandas as pd
import xml.etree.ElementTree as ET
class truncateDB(Abstract):
    
    def __init__(self, fila, columna, nombre):
        self.nombre = nombre
        super().__init__(fila, columna)

    def interpretar(self,environment):
        nombre = self.nombre
        tree = ET.parse(f'./src/data/xml/{nombre}.xml')
        root = tree.getroot()

        # Obtener todas las etiquetas <Table> y eliminar las etiquetas <Principal> dentro de ellas
        for table in root.findall(".//Table"):
            for principal in table.findall("Principal"):
                table.remove(principal)

        # Guardar el resultado en un nuevo archivo XML
        tree.write(f'./src/data/xml/{nombre}.xml', encoding='utf-8', xml_declaration=True)
