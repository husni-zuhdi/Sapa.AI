# [START cloudrun_helloworld_service]
# [START run_helloworld_service]
import os

from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)

# Home Service
@app.route("/")
def hello_world():
    name = os.environ.get("NAME", "to Sapa.AI")
    return jsonify(name)

# Panick Service
@app.route("/panick", methods=['GET', 'POST', 'DELETE'])
def panick():
    return

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
# [END run_helloworld_service]
# [END cloudrun_helloworld_service]
