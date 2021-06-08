import os
import json
from google.cloud import speech_v1p1beta1

def transcribe_sound(gcs_uri):
    """Asynchronously transcribes the audio file specified by the gcs_uri."""

    # Set cloud run backend service account key
    os.environ['GOOGLE_APPLICATION_CREDENTIALS']="key.json"

    client = speech_v1p1beta1.SpeechClient()

    audio = speech_v1p1beta1.RecognitionAudio(uri=gcs_uri)

    config = speech_v1p1beta1.RecognitionConfig(
        encoding=speech_v1p1beta1.RecognitionConfig.AudioEncoding.MP3,
        language_code="id-ID",
        sample_rate_hertz=44100,
    )

    # Wait for each sound file transcripted
    operation = client.long_running_recognize(config=config, audio=audio)
    response = operation.result(timeout=90)

    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    text = ""
    for result in response.results:
        text += result.alternatives[0].transcript
    return text

# # Test object
# import stt
# gcs_uri="gs://sapaai-bucket/audio/test/test_3.mp3"
# var=stt.transcribe_sound(gcs_uri)
