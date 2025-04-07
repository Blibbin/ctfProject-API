#!/usr/local/bin/python3

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def pre_challange():
    return jsonify({
        "message": "Check robots?"
    }), 200

@app.route('/api/start', methods=['GET'])
def start_challenge():
    return jsonify({
        "message": "Welcome to the CTF challenge",
        "hint": "Try examining the response headers for your next clue"
    }), 200, {'X-Next-Endpoint': '/api/headers'}

@app.route('/api/headers', methods=['GET'])
def header_challenge():
    if request.headers.get('CTF-Token') == '05262006':
        return jsonify({"message": "Success! Flag: flag{the_flag}"}), 200
    return jsonify({"message": "Incorrect headers provided"}), 403

@app.route('/api/auth', methods=['POST'])
def get_token():
    if request.json and request.json.get('username') == 'admin':
        token = 'fake_jwt_token_for_demo'  # Replace with actual JWT generation logic
        return jsonify({"token": token})
    return jsonify({"error": "Authentication failed"}), 401

@app.route('/api/admin', methods=['GET'])
def admin_endpoint():
    token = request.headers.get('Authorization', '').replace('Bearer ', '')
    if token == 'fake_jwt_token_for_demo':  # Replace with actual token validation logic
        return jsonify({"flag": "HTB{adm1n_t0k3n_byp4ss}"})
    return jsonify({"error": "Not authorized"}), 403

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
