import ml
import stt

uri = "gs://sapaai-bucket/audio/test/test.flac"
text = stt.transcribe_sound(uri)

instances=[text['transcript']]
print(instances)
version="v0_2"
pred_test = ml.predict_json(instances, version)
print(pred_test)