#!/usr/bin/env python3
"""Module for Flask APp"""


from flask import Flask, request, jsonify
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
