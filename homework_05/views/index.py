from flask import Blueprint
from flask import render_template

index_app = Blueprint("index_app", __name__, template_folder='templates')
AUTHORS_DATA = {
    1: "Марк Твен",
    2: "Леонард Луис Левинсон",
    3: "А.С. Пушкин",
}
# AUTHORS_TEXT = {}
# with open("static/content.txt") as file:
#     for line in file:
#         key, value = line.split(':')
#         AUTHORS_TEXT[key] = value


@index_app.route('/', endpoint="home")
def show_home():
    return render_template("/home.html", authors=AUTHORS_DATA)  # , authors_txt=AUTHORS_TEXT


@index_app.route('/about/', endpoint="about")
def show_about():
    return render_template("/about.html")
