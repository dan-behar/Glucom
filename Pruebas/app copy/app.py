  
from flask import Flask, render_template, request, url_for, redirect
from jinja2 import Template, FileSystemLoader, Environment
from datetime import datetime
# Convertimos un string con formato <día>/<mes>/<año> en datetime

domain = "0.0.0.0:5000/"
templates = FileSystemLoader('templates')
environment = Environment(loader = templates)

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form['name']
        hora = request.form['appt']
        print(name,hora)
        print(datetime.strptime(hora, '%H:%M'))
        print(hora)
    return render_template("register.html")

@app.route("/rango", methods=["GET", "POST"])
def rango():
    return render_template("rango.html")

@app.route("/graficas", methods=["GET", "POST"])
def gra():
    return render_template("graficas.html")

@app.route("/tabla", methods=["GET", "POST"])
def ta():
    return render_template("tabla.html")

@app.route("/aceleracion", methods=["GET", "POST"])
def ace():
    return render_template("aceleracion.html")

@app.route("/promedio", methods=["GET", "POST"])
def pro():
    return render_template("promedio.html")

@app.route("/meta", methods=["GET", "POST"])
def met():
    return render_template("meta.html")

@app.route("/tendencia", methods=["GET", "POST"])
def ten():
    return render_template("tendencia.html")

@app.route("/resumen", methods=["GET", "POST"])
def res():
    return render_template("resumen.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)