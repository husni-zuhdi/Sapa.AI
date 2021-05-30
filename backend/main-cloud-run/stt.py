import os
import json
from google.cloud import speech

# Set env variable
os.environ['GOOGLE_APPLICATION_CREDENTIALS']="main_key.json"

# Test object
# import stt
# gcs_uri="gs://sapaai-bucket/audio/test/test.flac"
# var=stt.transcribe_sound(gcs_uri)


def transcribe_sound(gcs_uri):
    """Asynchronously transcribes the audio file specified by the gcs_uri."""

    client = speech.SpeechClient()

    audio = speech.RecognitionAudio(uri=gcs_uri)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.FLAC,
        audio_channel_count=2,
        language_code="id-ID",
    )

    # Wait for each sound file transcripted
    operation = client.long_running_recognize(config=config, audio=audio)
    response = operation.result(timeout=90)

    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    for result in response.results:
         text = {"transcript":result.alternatives[0].transcript}
    return text