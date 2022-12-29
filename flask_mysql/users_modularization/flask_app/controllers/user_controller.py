from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.users import User


@app.route('/')
def index():
    return redirect('/create_user')

@app.route('/form')
def form():
    return render_template('create.html')

@app.route('/create_user', methods=['POST'])
def create():
    data = {
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'email':request.form['email']
    }
    User.save(data)
    print(data)
    return redirect('/')

@app.route('/create_user', methods = ['GET'])
def get_user():
    users = User.get_all()
    return render_template('index.html', users = users)