from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.ninjas_model import Ninja
from flask_app.models.dojos_model import Dojo

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()
    return render_template('index.html', dojos = dojos)

@app.route('/create_dojo', methods=['POST'])
def create():
    data = {
        'name':request.form['name']
    }
    Dojo.save(data)
    print(data)
    return redirect('/')

@app.route('/dojos/<int:dojo_id>/<name>')
def dojo_ninjas(dojo_id, name):
    dojo_id = {
        'id': id
    }
    dojo_name = {
        'name': name
    }
    dojo = Dojo.get_ninjas(dojo_name)
    return render_template('show_dojos.html', dojo = dojo)