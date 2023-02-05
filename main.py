__version__ = '1.0'
__author__ = 'Julian Camilo Builes Serrano'

__version__ = '1.0'
__author__ = 'Julian Camilo Builes Serrano'

from flask import Flask, make_response, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
app.config[
    "SECRET_KEY"
] = "1dafafghsdsf5378167uevsbg423)(dfghj98797781234741arfcshzgwffzgnssaerASXMHMRMDwefsrvs8945)(/%#"
app.secret_key = "test_secret"

@app.route("/", methods=["GET"])
def main():
    return make_response(jsonify(["hola"]))