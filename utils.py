from typing import Iterable, Optional
import re


def query_builder(iterable_var: Iterable, cmd: Optional[str], value: Optional[str]) -> Iterable:
    mapped_data = map(lambda v: v.strip(), iterable_var)

    if cmd == 'unique':
        return set(mapped_data)

    if value:
        if cmd == 'filter':
            return filter(lambda x: value in x, mapped_data)
        elif cmd == 'regex':
            regex = re.compile(value)
            return filter(lambda x: regex.search(x), mapped_data)
        elif cmd == 'map':
            arg = int(value)
            return map(lambda x: x.split(' ')[arg], mapped_data)
        elif cmd == 'limit':
            arg = int(value)
            return list(mapped_data)[:arg]
        elif cmd == 'sort':
            reverse = True if value == 'desc' else False
            return sorted(iterable_var, reverse=reverse)
    return mapped_data
