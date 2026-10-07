from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return f"""
    Toto je můj webový server!!!
    <br>
    <a href="{url_for('about_school')}">O škole</a>
    """


@app.route('/o-skole')
def about_school():
    return "Toto je stránka o škole."


@app.route('/student/<name>')
def student(name):
    return f"Toto je stránka o studentovi {name}."


@app.route('/predmet/<int:id>')
def subject(id):
    return f"Detail předmětu číslo {id}."


@app.route('/soucet/<int:a>/<int:b>')
def sum_numbers(a, b):
    return f"Součet čísel {a} a {b} je {a + b}."
