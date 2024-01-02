from datetime import date
import datetime
from src.ejecucion.type import Type
from src.expresiones.variable import Variable
from src.abstract.abstractas import Abstract


class Set_(Abstract):
    def __init__(self, row, column, id_, value):
        super().__init__(row, column)
        self.id = id_
        self.valor = value

    def accept(self, visitor, environment):
        visitor.visit(self, environment)

    def interpretar(self, environment):

        value = self.valor.interpretar(environment)

        variable = environment.getVariable(self.id)

        if isinstance(value, str):
            variable.value = value
        elif isinstance(value, dict):
            lista_resultado = value.get('resultado', [])
            if len(lista_resultado) >= 2:
                segundo_resultado = lista_resultado[1]
                print(segundo_resultado[0])
                if segundo_resultado[0] == "---":
                    if variable.type == Type.INT:
                        segundo_resultado[0] = 0
                    elif variable.type == Type.DECIMAL:
                        segundo_resultado[0] = 0.0
                    elif variable.type == Type.TEXT:
                        segundo_resultado[0] = ""
                    elif variable.type == Type.DATE:
                        segundo_resultado[0] = date.today()
                    elif variable.type == Type.DATETIME:
                        segundo_resultado[0] = datetime.datetime.now()
                    elif variable.type == Type.BIT:
                        segundo_resultado[0] = False
                value = self.tipoFuncionSistema(segundo_resultado[0])
                variable.value = value.value
        else:
            variable.value = value.value

        return self

    def tipoFuncionSistema(self, valor):
        variable = Variable()

        print("tipo de dato", type(valor))

        if isinstance(valor, str):
            variable.value = str(valor)
            variable.type = Type.TEXT
        elif isinstance(valor, int):
            variable.value = int(valor)
            variable.type = Type.INT
        elif isinstance(valor, float):
            variable.value = float(valor)
            variable.type = Type.DECIMAL
        elif isinstance(valor, date):
            variable.value = valor
            variable.type = Type.DATE
        elif isinstance(valor, datetime):
            variable.value = valor
            variable.type = Type.DATETIME
        elif isinstance(valor, bool):
            variable.type = Type.BIT
            if valor:
                variable.value = int(1)
            else:
                variable.value = int(0)
        return variable