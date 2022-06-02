from flask import Flask, request
from utils import get_log_list, set_filter, set_map
app = Flask(__name__)


@app.route("/perform_query")
def perform_query():
    # Принимаем данные из запроса
    data = request.args
    file_name = data['file_name'] or None
    cmd1 = data['cmd1'] or None
    value1 = data['value1'] or None
    cmd2 = data['cmd2'] or None
    value2 = data['value2'] or None

    if file_name is not None:
        list_log = get_log_list(file_name)
        if list_log:
            #  Фильтрация данных
            if cmd1 == 'filter' and len(value1) > 0:
                list_log = set_filter(list_log, value1)
            elif cmd2 == 'filter' and len(value2) > 0:
                list_log = set_filter(list_log, value2)

            #  Изменение формата вывода
            if cmd1 == 'map' and value1.isdigit():
                list_log = set_map(list_log, int(value1))
            elif cmd2 == 'map' and value2.isdigit():
                list_log = set_map(list_log, int(value2))

            #  Уникальные значения
            if cmd1 == 'unique' or cmd2 == 'unique':
                list_log = list(set(list_log))

            # Сортировка данных
            if cmd1 == 'sort':
                if value1 == 'desc':
                    list_log = sorted(list_log, reverse=True)
                else:
                    list_log = sorted(list_log, reverse=False)
            elif cmd2 == 'sort':
                if value2 == 'desc':
                    list_log = sorted(list_log, reverse=True)
                else:
                    list_log = sorted(list_log, reverse=False)

            #  Лимит вывода
            if cmd1 == 'limit' and value1.isdigit():
                list_log = list_log[:int(value1)]
            elif cmd2 == 'limit' and value2.isdigit():
                list_log = list_log[:int(value2)]

            list_log = [item + '\n' for item in list_log]

            return app.response_class(list_log, 200, content_type="text/plain")
        else:
            return 'Файл не найден или пустой', 404
    else:
        return 'Не указано имя файла', 400


if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost", port=5000)
