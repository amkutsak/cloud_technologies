# Лабораторная работа 2
## Цель работы: 
Выявить и сравнить плохую и хорошую практику использования Dockerfile при работе с контейнерами.
## Установка Docker
Установим на MacOs приложение Docker c официального сайта. Для дальнейшей настройки будет использовать терминал. Пропишем следующие команды:
```
 sudo hdiutil attach Docker.dmg
 sudo /Volumes/Docker/Docker.app/Contents/MacOS/install
 sudo hdiutil detach /Volumes/Docker
```
## Ход работы:
Необходимо создать две папки для плохого и хорошего докер файла, внутри папок помимо самого докер файла также находится файл с кодом на питон и файл для хранения версии используемых библиотек.
Содержимое контейнера это простой код на питоне, которыймы расположим на http сервере.
Создадим файл с кодом на питоне - app.py:
```
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Всем привет, это плохой докер файл:(, если вам интересно почему, переходите в отчет!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)

```
Аналогичный файл хранится в папке с хорошим докер файлом.
Ниже представлен файл для хранения версий библиотек:
```
Flask==2.0.1
Werkzeug==2.0.1
```
Теперь напишем код для плохого Dockerfile:
```
FROM python:3.8
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt
COPY . /
RUN pip install gunicorn
EXPOSE 9090
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:9090", "app:app"]

```
