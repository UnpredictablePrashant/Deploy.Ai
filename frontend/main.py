# this will be the flask file that will orchestrate 
# the routing of the html pages depending upon the requests

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about_us():
    return render_template('aboutus.html')

@app.route('/contribute')
def contribute():
    return render_template('contribute.html')

@app.route('/howitworks')
def how_it_works():
    return render_template('howitworks.html')

@app.route('/loginsuccess')
def login_success():
    return render_template('loginsuccess.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/loginsuccess/docs')
def docs():
    return render_template('docs.html')

@app.route('/loginsuccess/tutorials')
def tutorials():
    return render_template('tutorials.html')

@app.route('/loginsuccess/needhelp')
def needhelp():
    return render_template('needhelp.html')


if __name__ == '__main__':
    app.run(debug=True)
