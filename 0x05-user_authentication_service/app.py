#!/usr/bin/env python3
"""Module for Flask APp"""


from flask import Flask, request, jsonify, abort, redirect
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    """Index page"""
    return jsonify({'message': 'Bienvenue'})


@app.route('/users', methods=['POST'])
def register():
    """Route for registering a user"""
    email = request.form.get('email')
    passwrd = request.form.get('password')

    try:
        AUTH.register_user(email, passwrd)
        return jsonify({'email': email, 'message': 'user created'})

    except ValueError:
        return jsonify({'message': 'email already registered'}), 400


@app.route('/sessions', methods=['POST'])
def login():
    """Route for loggin in a user"""
    email = request.form.get('email')
    pw = request.form.get('password')

    if not (AUTH.valid_login(email=email, password=pw)) or not email or not pw:
        abort(401)

    session_id = AUTH.create_session(email=email)
    response = jsonify({'email': email, 'message': 'logged in'})
    response.set_cookie('session_id', session_id)
    return response


@app.route('/sessions', methods=['DELETE'])
def logout():
    """Route for logging out a user"""
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)

    if user and session_id:
        AUTH.destroy_session(session_id)
        return redirect('/')

    else:
        abort(403)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
