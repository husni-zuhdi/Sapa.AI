Creating a Speech-to-Text Cloud:
--------------------------------
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
6. Next..