# this will be the flask file that will orchestrate 
# the routing of the html pages depending upon the requests

from flask import Flask, render_template
from flask import redirect, session, jsonify, request

app = Flask(__name__)
app.secret_key = 'a_random_secret_key'


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
    # Set user-specific session data
    session['user_id'] = 'the_id_of_the_user'
    session['user_name'] = 'the_name_of_the_user'
    # You can set other user-specific details as well
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

################################################################
################################ chatbot functionality################################

def get_chatbot_response(user_id, message):
    # Here, integrate with your actual chatbot service
    # For demonstration, we'll just echo the message
    return f"Echo: {message}"

@app.route('/send_message', methods=['POST'])
def handle_message():
    user_id = session.get('user_id')
    if not user_id:
        # Handle the case where there's no user session
        return jsonify({'error': 'User not logged in or session expired'}), 403

    message = request.json.get('message')
    if not message:
        return jsonify({'error': 'No message provided'}), 400

    response_message = get_chatbot_response(user_id, message)
    return jsonify({'message': response_message})


################################ end of chatbot #################################
######################################################################################


@app.route('/logout')
def logout():
    # Perform any necessary cleanup, like invalidating your app's session
    session.clear()
    # Redirect to Cognito's logout endpoint
    cognito_logout_url = (
        "https://ai-deploy.auth.ap-southeast-1.amazoncognito.com/logout?"
        "client_id=7778obvq454q15r0s3ll32l9f7&"  # Your Cognito App Client ID
        "logout_uri=https://dynalink.in/"  # Your sign-out URL
    )
    return redirect(cognito_logout_url)

if __name__ == '__main__':
    app.run(debug=True)
