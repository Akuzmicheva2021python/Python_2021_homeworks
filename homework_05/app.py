"""
Домашнее задание №4
Первое веб-приложение

создайте базовое приложение на Flask
создайте index view /
добавьте страницу /about/, добавьте туда текст
создайте базовый шаблон (используйте https://getbootstrap.com/docs/5.0/getting-started/introduction/#starter-template)
в базовый шаблон подключите статику Bootstrap 5 и добавьте стили, примените их
в базовый шаблон добавьте навигационную панель nav (https://getbootstrap.com/docs/5.0/components/navbar/)
в навигационную панель добавьте ссылки на главную страницу / и на страницу /about/ при помощи url_for
"""
from flask import Flask

from views.index import index_app

app = Flask(__name__)
app.register_blueprint(index_app, url_prefix='/')


@app.route("/")
def hello():
    return "<p>Hello, World!</p>"


if __name__ == '__main__':
    app.run(debug=True)
