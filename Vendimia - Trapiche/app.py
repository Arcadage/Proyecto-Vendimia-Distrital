#import pandas as pd
import json
from flask import Flask, render_template, request, redirect
from files import routes_files
from funciones import leer_json, aExcel, SumarVotos


app = Flask(__name__)
app.register_blueprint(routes_files)

@app.route('/',methods=['GET','POST'])
def prode1():
    leer = leer_json()
    cadi = request.args.get('candidata')
    if cadi == 'Votar Geraldina':
        SumarVotos("1")
        aExcel()
        return redirect('/') 
    elif cadi == 'Votar Catalina':
        SumarVotos("2")
        aExcel()
        return redirect('/')
    elif cadi == 'Votar Katherina':
        SumarVotos("3")
        aExcel()
        return redirect('/')         
    return render_template('prode.html',leer=leer)

@app.route('/votos',methods=['GET','POST'])
def votos():
    leer = leer_json()
    lista = []
    for i in leer.values():
     lista.append(i["Nombre"])
     lista.append(i["Votos"])

    return render_template('votos.html',lista=lista)

if __name__ == '__main__':
 app.run( debug=True )