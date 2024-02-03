# this will be the flask file that will orchestrate 
# the routing of the html pages depending upon the requests

from flask import Flask, render_template, redirect, url_for
from flask_cognito_lib import *
# from flask_cognito_lib import CognitoAuth, cognito_auth_required

app = Flask(__name__)

# Configuration: Replace these with your actual settings
app.config['COGNITO_REGION'] = 'ap-southeast-1'
app.config['COGNITO_USERPOOL_ID'] = 'ap-southeast-1_2WfO8UmdC'
app.config['COGNITO_CLIENT_ID'] = '7778obvq454q15r0s3ll32l9f7'
# app.config['COGNITO_CLIENT_SECRET'] = 'YOUR_CLIENT_SECRET'
app.config['COGNITO_DOMAIN'] = 'https://ai-deploy.auth.ap-southeast-1.amazoncognito.com' # e.g., 'your-domain.auth.ap-southeast-1.amazoncognito.com'
app.config['COGNITO_REDIRECT_URI'] = 'https://dynalink.in/loginsuccess' # e.g., 'https://your-app.com/auth/callback'

cognito_auth = CognitoAuth(app)

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

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    return cognito_auth.get_sign_in_url()

@app.route('/auth/callback')
@cognito_auth.callback_handler
def auth_callback(token_data):
    # Handle the callback and use token_data, e.g., save it in the session
    # Then redirect the user to another page, such as their profile or dashboard
    return redirect(url_for('login_success'))

@app.route('/loginsuccess')
@cognito_auth_required
def login_success():
    # Access the user's token data (if needed)
    token_data = cognito_auth.get_token_data()
    return render_template('loginsuccess.html', token_data=token_data)

@app.route('/loginsuccess/docs')
@cognito_auth_required
def docs():
    return render_template('docs.html')

@app.route('/loginsuccess/tutorials')
@cognito_auth_required
def tutorials():
    return render_template('tutorials.html')

@app.route('/loginsuccess/needhelp')
@cognito_auth_required
def needhelp():
    return render_template('needhelp.html')

if __name__ == '__main__':
    app.run(debug=True)
