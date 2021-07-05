  
from flask import Flask, render_template, request, url_for, redirect
from jinja2 import Template, FileSystemLoader, Environment
from datetime import datetime
from datos import Datos 
# Convertimos un string con formato <día>/<mes>/<año> en datetime

domain = "0.0.0.0:5000/"
templates = FileSystemLoader('templates')
environment = Environment(loader = templates)

app = Flask(__name__)

global name 
name = "" 
global hora 
hora = 0.0 
global muestra 
muestra = []
global data
data = '' 
global horaMuestra 
horaMuestra = []
global glucoMuestra 
glucoMuestra = []
global consMuestra 
consMuestra = []


@app.route("/", methods=["GET", "POST"])
def register():
    global name
    global hora 
    global data 
    if request.method == "POST":
        name = request.form['name']
        hora = request.form['appt']
        print(name,hora)

        (h, m) = hora.split(':')
        hora = int(h) + int(m)/60 
        data = Datos('datos.xlsx',hora)
        return redirect("/rango", 301)
    return render_template("register.html")

@app.route("/rango", methods=["GET", "POST"])
def rango():
    global data
    global muetra 
    global horaMuestra
    global glucoMuestra
    global consMuestra
    if request.method == "POST":
        date1 = request.form['date1']
        date2 = request.form['date2']
        date1 = datetime.strptime(date1, '%Y-%m-%d')
        date2 = datetime.strptime(date2, '%Y-%m-%d')
        # print(date1, date2)
        muestra = data.muestra(date1, date2)
        for i in range(len(muestra)):
            horaMuestra.append(muestra[i][2])
            glucoMuestra.append(muestra[i][1])
            consMuestra.append(muestra[i][3])
        print(horaMuestra)
        print(glucoMuestra)
        print(consMuestra)
        
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