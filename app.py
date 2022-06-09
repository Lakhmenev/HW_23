from flask import Flask, request
from pathlib import Path
from werkzeug.exceptions import BadRequest
from utils import query_builder

app = Flask(__name__)


@app.route("/perform_query")
def perform_query():
    # Принимаем данные из запроса
    file_name = request.args['file_name'] or None
    cmd1 = request.args['cmd1'] or None
    value1 = request.args['value1'] or None
    cmd2 = request.args['cmd2'] or None
    value2 = request.args['value2'] or None

    if file_name is None:
        return BadRequest(description='Не задано имя  файла')

    file_path = Path.cwd() / 'data' / file_name
    if Path.exists(file_path):
        with open(file_path, 'r', encoding='utf8') as fd:
            result = query_builder(fd, cmd1, value1)
            result = query_builder(result, cmd2, value2)
            result = '\n'.join(result)

        return app.response_class(result, 200, content_type="text/plain")
    else:
        return BadRequest(description=f'Файл {file_name} не найден')


if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost", port=5000)
