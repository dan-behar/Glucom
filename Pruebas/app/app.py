  
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

@app.route("/home", methods=["GET", "POST"])
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)