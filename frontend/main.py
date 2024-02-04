# this will be the flask file that will orchestrate 
# the routing of the html pages depending upon the requests

from flask import Flask, render_template
from flask import redirect

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
    cognito_url = "https://ai-deploy.auth.ap-southeast-1.amazoncognito.com/oauth2/authorize?response_type=code&client_id=7778obvq454q15r0s3ll32l9f7&redirect_uri=https://dynalink.in/loginsuccess"
    return redirect(cognito_url)

@app.route('/loginsuccess/docs')
def docs():
    return render_template('docs.html')

@app.route('/loginsuccess/tutorials')
def tutorials():
    return render_template('tutorials.html')

@app.route('/loginsuccess/needhelp')
def needhelp():
    return render_template('needhelp.html')

@app.route('/logout')
def logout():
    # Perform any necessary cleanup, like invalidating your app's session
    
    # Redirect to Cognito's logout endpoint
    cognito_logout_url = (
        "https://ai-deploy.auth.ap-southeast-1.amazoncognito.com/logout?"
        "client_id=7778obvq454q15r0s3ll32l9f7&"  # Your Cognito App Client ID
        "logout_uri=https://dynalink.in/"  # Your sign-out URL
    )
    return redirect(cognito_logout_url)

if __name__ == '__main__':
    app.run(debug=True)
