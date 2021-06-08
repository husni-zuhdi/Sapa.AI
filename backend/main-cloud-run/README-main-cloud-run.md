# Main-cloud-run

## Main (main.py)

Sapa.AI API use python runtime. There are two route, forms and panick.

1. Forms route - Save forms report to Realtime Database

2. Panick route - Save panick report and implement Speech to Text API and our Machine Learning model

## Speech to text API (stt.py)

Transcribe the recorded voices into text. We use Speech to Text API provided by Google

How to use Speech-to-Text API:

1. Create an API key (credential)
2. Enable Cloud Speech-to-Text API with console
2. Download API key like in json format and save it in this folder with name "key.json"
3. Create Speech API request in python with uri as an argument. Example

    import stt
    uri = "gs://sapaai-bucket/audio/test/test_3.mp3"
    text = stt.transcribe_sound(uri)


4. See the result use 'print(text)'

## Machine Learning API (ml.py)

Classify the transcribed test into 8 services victim need.

How to use our Multi Classification Model

1. Create an API key (credential)
2. Download API key like in json format and save it in this folder with name "key.json"
3. Create request to our model in python with instance and model version as arguments. For example

    from ml import predict_json
    instances=["saya anak yang baik tetapi sering dipukuli paman saya karena selalu menolak ketika diajak bekerja di pasar"]
    version="v3"
    test = predict_json(instances, version)

4. See the result use 'print(text)'

## Deploy to Google Cloud Platform

You can run deploy.sh from your linux environment. Make sure you set the GOOGLE_CLOUD_PROJECT in the deploy.sh file.
