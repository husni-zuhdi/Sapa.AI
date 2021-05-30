# Import packages
import os
from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from google.auth.environment_vars import PROJECT

# Import from py file
from stt import transcribe_sound
from ml import predict_json

app = Flask(__name__)

# Definisi env variabel dalam linux
os.environ['GOOGLE_APPLICATION_CREDENTIALS']="main_key.json"

# Form Service
@app.route("/form", methods=['GET', 'POST', 'DELETE'])
def fform():
    form = os.environ.get("NAME", "to Form")
    return jsonify(form)

# Panick Service
@app.route("/panick", methods=['GET', 'POST', 'DELETE'])
def fpanick():
    # Text-to-speech
    gcs_uri="gs://sapaai-bucket/audio/test/test.flac"
    text = stt.transcribe_sound(gcs_uri)

    # Variabel-variabel model
    project="sapaai"
    region="asia-southeast-1"
    model="multiclass"
    instances=[[text['transcript']]]
    version="v0_2"

    predict = predict_json(project, region, model, instances, version)

    return predict

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))