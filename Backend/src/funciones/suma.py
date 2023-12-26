from ..abstract import Abstract
from src.ejecucion.type import Type
from src.ast import TableColumn


class Suma(Abstract):
    def __init__(self, fila, columna, value):
        super().__init__(fila, columna)
        self.value = value
        self.tipo = Type.DECIMAL

    def __str__(self):
        return "SUMA"

    def accept(self, visitor, environment):
        if not isinstance(self.value, int):
            self.value.accept(visitor, environment)
        visitor.visit(self, environment)

    # no se si le enviamos el tipo de dato asi com date
    def interpretar(self, environment):
        records = environment.select_records
        if len(records) == 0:
            return 0

        if not isinstance(self.value, int):
            if self.value.tipo not in [Type.INT, Type.DECIMAL]:
                return 0

        aux_record = environment.record
        suma = 0
        for record in records:
            # Verificar si la llave es un nombre o un número
            environment.one_record = True
            if isinstance(self.value, int):
                try:
                    key = self.value
                    keys = list(record.keys())
                    if key < len(keys):
                        val = record[keys[key]]
                        val = float(val)
                        suma += val
                except ValueError:
                    suma += 0

            else:
                environment.record = record
                result = self.value.interpretar(environment)
                val = result if isinstance(result, (int, float)) else 0
                suma += val

            environment.record = aux_record
        return float(suma)
