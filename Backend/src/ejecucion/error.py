import json


class T_error():
    def __init__(self, tipo, token, descripcion, row, column):
        self.tipo = tipo
        self.token = token
        self.description = descripcion
        self.row = row
        self.column = column

    def toString(self):
        valor = self.token
        if not isinstance(self.token, str):
            valor = str(valor)
        return "Tipo: {} Token: {} Descripcion: {} Linea: {} Columna: {}".format(self.tipo, valor, self.description, self.row, self.column)

    def to_dict(self):
        return {
            "tipo": self.tipo,
            "token": str(self.token) if not isinstance(self.token, str) else self.token,
            "descripcion": self.description,
            "linea": self.row,
            "columna": self.column
        }

    def to_json(self):
        return json.dumps(self.to_dict(), indent=2)

