from flask import Flask, request
from utils import get_log_list, query_builder

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
            list_log = query_builder(list_log, cmd1, value1)
            list_log = query_builder(list_log, cmd2, value2)

            #  Добавим перенос строки для вывода
            list_log = [item + '\n' for item in list_log]

            return app.response_class(list_log, 200, content_type="text/plain")
        else:
            return 'Файл не найден или пустой', 404
    else:
        return 'Не указано имя файла', 400


if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost", port=5000)
