from flask import Flask, render_template, request, redirect

from users import User

app = Flask(__name__)
app.secret_key = "flask is the worst"

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
    return redirect('/')

@app.route('/create_user', methods = ['GET'])
def get_user():
    users = User.get_all()
    return render_template('index.html', users = users)

@app.route('/user/edit/<int:id>')
def edit(id):
    data = {
        "id":id
    }
    return render_template("show.html", user = User.get_one(data))

@app.route('user/<int:id>')
def show():
        pass

@app.route('/user/update', methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)