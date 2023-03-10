from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.ninjas_model import Ninja
from flask_app.models.dojos_model import Dojo

@app.route('/ninjas')
def ninjas():
    dojos = Dojo.get_all()
    return render_template('ninjas.html', dojos = dojos)

@app.route('/ninjas', methods=['POST'])
def create_ninja():
    data = {
        'dojo_id':request.form['dojo'],
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'age':request.form['age']
    }
    Ninja.save(data)
    print(data)
    return redirect('/')