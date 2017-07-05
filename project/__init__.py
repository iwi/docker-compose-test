# project/__init__.py

from flask import Flask, jasonify

# instantiate the app
app = Flask(__name__)

@app.route('/ping', mdthods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })
