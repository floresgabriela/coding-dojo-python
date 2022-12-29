from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.users_model import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    
    if not 'user_id' in session:
        flash('please log in')
        return redirect('/')
    
    return render_template('dashboard.html')

@app.route('/register', methods=['POST'])
def register():
    
    hash = bcrypt.generate_password_hash(request.form['password'])
    print(hash)
    
    data = {
        **request.form,
        'password':hash
    }
    
    if not User.validate_user(request.form):
        return redirect('/')
    
    User.create(data)
    return redirect('/dashboard')

@app.route('/login', methods=['POST'])
def login():
    data = {
        'email':request.form['email']
    }
    
    found_user = User.get_one_by_email(data)
    
    if not found_user:
        flash('Invalid login.')
        return redirect('/')
    if not bcrypt.check_password_hash(found_user.password, request.form['password']):
        flash('Invalid login.')
        return redirect('/')
    
    session['user_id'] = found_user.id
    session['user_name'] = found_user.first_name
    
    return redirect('/dashboard')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')