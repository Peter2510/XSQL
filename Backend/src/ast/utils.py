def add_prefix_to_keys(list_of_dicts, prefix):
    new_list_of_dicts = []

    for original_dict in list_of_dicts:
        new_dict = {}
        for key, value in original_dict.items():
            new_key = f"{prefix}.{key}"
            new_dict[new_key] = value
        new_list_of_dicts.append(new_dict)

    return new_list_of_dicts


def filter_where_clause(expr, environment):
    def filter_by(record) -> bool:
        environment.record = record
        value = expr.interpretar(environment)
        return bool(value)

    return filter_by


def apply_column_expressions(expr_lst, environment):
    def alter_record(record):
        environment.record = record
        new_dict = {}
        for expr in expr_lst:
            name = str(expr)
            new_dict[name] = expr.interpretar(environment)

        return new_dict

    return alter_record
