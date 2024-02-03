from os import environ, urandom
from dotenv import load_dotenv
from flask import Flask, render_template, redirect, session, url_for
from flask_cognito_lib import CognitoAuth
from flask_cognito_lib.decorators import (
    auth_required,
    cognito_login,
    cognito_login_callback,
    cognito_logout,
)
from flask_cognito_lib.exceptions import (
    AuthorisationRequiredError,
    CognitoGroupRequiredError,
)

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))

app = Flask(__name__)

# Configuration: Replace these with your actual settings
app.config['SECRET_KEY'] = environ.get("SECRET_KEY", urandom(32))
app.config['COGNITO_REGION'] = 'ap-southeast-1'
app.config['COGNITO_USERPOOL_ID'] = 'ap-southeast-1_2WfO8UmdC'
app.config['COGNITO_CLIENT_ID'] = '7778obvq454q15r0s3ll32l9f7'
app.config['COGNITO_DOMAIN'] = 'https://ai-deploy.auth.ap-southeast-1.amazoncognito.com' 
app.config['COGNITO_REDIRECT_URI'] = 'https://dynalink.in/loginsuccess'
app.config['COGNITO_LOGOUT_URL'] = 'https://dynalink.in/'  # You need to add this
app.config['COGNITO_COOKIE_AGE_SECONDS'] = '300'  # You need to add this

cognito_auth = CognitoAuth(app)

@app.route('/')
def index():
    return render_template('index.html')

# ... other routes ...

@app.route('/login')
@cognito_login
def login():
    # Logic handled by decorator
    pass

@app.route('/auth/callback')
@cognito_login_callback
def auth_callback():
    # Logic handled by decorator
    return redirect(url_for('login_success'))

@app.route('/loginsuccess')
@auth_required()
def login_success():
    return jsonify(session)

@app.errorhandler(AuthorisationRequiredError)
def auth_error_handler(err):
    return redirect(url_for("login"))

@app.route('/logout')
@cognito_logout
def logout():
    # Logic handled by decorator
    pass

@app.route('/postlogout')
def postlogout():
    return redirect(url_for("index"))

# ... other routes ...

if __name__ == '__main__':
    app.run(debug=True, port=5000)
