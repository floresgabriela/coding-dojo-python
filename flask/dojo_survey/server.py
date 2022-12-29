from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "secret"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results')
def results():
    return render_template('results.html')

@app.route('/post_results', methods=['POST'])
def post_results():
    session['name'] = request.form['name']
    session['locations'] = request.form['locations']
    session['languages'] = request.form['languages']
    session['comments'] = request.form['comments']
    return redirect('/results')

if __name__=="__main__":
    app.run(debug=True)