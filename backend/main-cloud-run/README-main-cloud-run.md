# Main-cloud-run

## Main (main.py)

Sapa.AI API use python runtime. There are two route, forms and panick.

1. Forms route - Save forms report to Realtime Database

2. Panick route - Save panick report and implement Speech to Text API and our Machine Learning model

## Speech to text API (stt.py)

Transcribe the recorded voices into text. We use Speech to Text API provided by Google

Creating a Speech-to-Text Cloud:

1. Create an API key (credential)
2. Enable Cloud Speech-to-Text API with console
2. Export API key like that (in SSH or cloudshell): export API_KEY=<YOUR_API_KEY>
3. Create Speech API request (fiile name ex: request.json)
4. Call the Speech API with syntax:

curl -s -H "Content-Type: application/json" \
    -H "Authorization: Bearer "$(gcloud auth application-default print-access-token) \
    https://speech.googleapis.com/v1/speech:recognize \
    -d @sync-request.json

5. cat result.json to view the transcription of .flac file (audio)
6. Next

## Machine Learning API (ml.py)

Classify the transcribed test into 8 services needed by victim.