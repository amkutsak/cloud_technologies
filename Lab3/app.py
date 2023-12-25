from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Всем привет, это хороший докер файл, если вам интересно почему, переходите в отчет:)'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
