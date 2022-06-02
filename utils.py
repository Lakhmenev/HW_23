from pathlib import Path


def get_log_list(log_name: str):
    file_path = Path.cwd() / 'data' / log_name
    log_list = []
    if Path.is_file(file_path):
        with open(file_path, 'r', encoding='utf8') as txt_file:
            for line in txt_file:
                line.replace('\n', '')
                log_list.append(line)
    return log_list


def get_format(in_string: str, col: int):
    temp_list = in_string.split(' ')
    out_string = temp_list[col]
    return out_string


def set_filter(in_list: list, filter_str: str):
    return list(filter(lambda x: filter_str in x, in_list))


def set_map(in_list: list, column: int):
    return list(map(lambda x: get_format(x, column), in_list))
