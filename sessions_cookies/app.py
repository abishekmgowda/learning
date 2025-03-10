from flask import Flask, session, request, redirect, url_for
import os

app = Flask(__name__)

# Secret key is required for session encryption
app.secret_key = os.urandom(24)

@app.route('/')
def home():
    """Display the homepage with session info"""
    username = session.get('username')
    if username:
        return f"Welcome back, {username}! <br><a href='/logout'>Logout</a>"
    return "Hello, Guest! <br><a href='/login'>Login</a>"

@app.route('/login')
def login():
    """Simulates user login by setting a session"""
    session['username'] = 'Abishek'  # Setting session value
    return redirect(url_for('home'))  # Redirect to home after login

@app.route('/logout')
def logout():
    """Clears the session when the user logs out"""
    session.pop('username', None)
    return redirect(url_for('home'))  # Redirect to home after logout

if __name__ == '__main__':
    app.run(debug=True)

