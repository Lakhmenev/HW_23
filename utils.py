from pathlib import Path


def get_log_list(log_name: str):
    file_path = Path.cwd() / 'data' / log_name
    log_list = []
    if Path.is_file(file_path):
        with open(file_path, 'r', encoding='utf8') as txt_file:
            for line in txt_file:
                log_list.append(line)

    #  Удаляем переносы строк и конечные пробелы
    log_list = [line.rstrip() for line in log_list]
    return log_list


def get_format(in_string: str, col: int):
    temp_list = in_string.split(' ')
    out_string = temp_list[col]
    return out_string


def set_filter(in_list: list, filter_str: str) -> list:
    return list(filter(lambda x: filter_str in x, in_list))


def set_map(in_list: list, column: int):
    return list(map(lambda x: get_format(x, column), in_list))


def query_builder(iterable_var: list, cmd, value) -> list:
    if cmd == 'unique':
        return list(set(iterable_var))

    if value:
        if cmd == 'filter':
            iterable_var = set_filter(iterable_var, value)

        elif cmd == 'map':
            iterable_var = list(map(lambda x: get_format(x, int(value)), iterable_var))

        elif cmd == 'limit':
            iterable_var = iterable_var[:int(value)]

        elif cmd == 'sort':
            if value == 'desc':
                iterable_var = sorted(iterable_var, reverse=True)
            else:
                iterable_var = sorted(iterable_var, reverse=False)

    return iterable_var
