from itertools import product


def add_prefix_to_keys(list_of_dicts, prefix):
    new_list_of_dicts = []

    for original_dict in list_of_dicts:
        new_dict = {}
        for key, value in original_dict.items():
            new_key = f"{prefix}.{key}"
            new_dict[new_key] = value
        new_list_of_dicts.append(new_dict)

    return new_list_of_dicts


def remove_prefix_to_keys(list_of_dicts, prefix):
    new_list_of_dicts = []

    for original_dict in list_of_dicts:
        new_dict = {}
        for key, value in original_dict.items():
            key_values = key.split(f"{prefix}.")
            new_key = key_values[1]
            new_dict[new_key] = value
        new_list_of_dicts.append(new_dict)

    return new_list_of_dicts


def filter_where_clause(expr, environment):
    def filter_by(record) -> bool:
        environment.record = record
        value = expr.interpretar(environment)
        return bool(value)

    return filter_by


def filter_where_delete(expr, environment):
    def filter_by(record) -> bool:
        environment.record = record
        value = expr.interpretar(environment)
        return not bool(value)

    return filter_by


def apply_column_expressions(expr_lst, environment):
    def alter_record(record):
        from src.ast import AllColumns
        from src.funciones import Contar, Suma
        if isinstance(expr_lst[0], AllColumns):
            return record
        environment.record = record
        new_dict = {}
        for expr in expr_lst:
            name = str(expr)
            new_dict[name] = expr.interpretar(environment)

        return new_dict

    return alter_record


def cartesian_product(*tables):
    # Obtener todas las combinaciones posibles de filas entre las tablas
    result = list(product(*tables))

    # Crear una lista de diccionarios para representar el resultado
    result_dicts = [dict(item for sublist in row for item in sublist.items()) for row in result]

    return result_dicts


def get_table_form(data: list[dict]):
    columns = list(data[0].keys())
    rows = []
    for record in data:
        rows.append(list(record.values()))

    return [columns, *rows]
