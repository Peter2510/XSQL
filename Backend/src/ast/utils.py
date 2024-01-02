from itertools import product
from src.ejecucion.type import Type


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


def apply_update_expressions(where_expr, assign_lst: list, environment):
    def update_columns(record):
        environment.record = record
        value = where_expr.interpretar(environment)
        needs_update = bool(value)
        if not needs_update:
            return record

        environment.altered_records += 1
        for assign in assign_lst:
            column_ref = assign.column_ref
            column_name = str(column_ref)
            expr = assign.expr
            new_value = str(expr.interpretar(environment))
            if expr.tipo == Type.TEXT and len(new_value) > column_ref.limit:
                new_value = new_value[:column_ref.limit]

            environment.record[column_name] = new_value

        return environment.record

    return update_columns


def get_column_expressions(expr_lst):
    return [dict((str(expr), '---') for expr in expr_lst)]


def cartesian_product(*tables):
    # Obtener todas las combinaciones posibles de filas entre las tablas
    result = list(product(*tables))

    # Crear una lista de diccionarios para representar el resultado
    result_dicts = [dict(item for sublist in row for item in sublist.items()) for row in result]

    return result_dicts


def get_table_form(data: list[dict]):
    data_len = len(data)

    columns = list(data[0].keys()) if data_len > 0 else ["No results"]
    rows = []
    for record in data:
        rows.append(list(record.values()))

    return [columns, *rows]
