#First Test : Test Speech to text API and Machine Learning Model
# import ml
# import stt
# uri = "gs://sapaai-bucket/audio/test/test_2.flac"
# text = stt.transcribe_sound(uri)

# input()
# input()

# instances=[text['transcript']]
# print(instances)
# input()
# input()
# version="v0_2"
# pred_test = ml.predict_json(instances, version)
# proced_test = {
#     "1 Layanan Hukum":pred_test[0][0],
#     "2 Layanan Medis":pred_test[0][1],
#     "3 Layanan Psikologis":pred_test[0][2],
#     "4 Layanan Rehabilitasi Sosial":pred_test[0][3],
#     "5 Layanan Jaminan Keselamatan":pred_test[0][4],
#     "6 Layanan Layanan Pendidikan":pred_test[0][5],
#     "7 Layanan Pengasuhan Pengganti":pred_test[0][6],
#     "8 Layanan Bantuan Sosial":pred_test[0][7]
# }
# print(proced_test)
# Seconde Test: Forms API test
import requests

BASE = "http://127.0.0.1:5000/"

# =====================Test Form route============================
# id_forms = 3
# data = {"id_users": 3,
#         "nama_korban_forms": "Husni",
#         "nama_tersangka_forms": "Husni Naufal Zuhdi",
#         "kronologi_forms": "husni memukul husni yang sedang main FF",
#         "flag_layanan1": 1,
#         "flag_layanan2": 1,
#         "flag_layanan3": "",
#         "flag_layanan4": "",
#         "flag_layanan5": "",
#         "flag_layanan6": "",
#         "flag_layanan7": "",
#         "flag_layanan8": 1,
#         "foto_forms": "",
#         "lokasi_forms": "depan kosan Husni",
#         "upload_date_forms": "dua hari lalu"}

# # Post Respones (v) PASSED
# response = requests.put(BASE + "form/" + str(id_forms), data)
# print(response)

# # Get Respones (v) PASSED
# response = requests.get(BASE + "form/" + str(id_forms))
# print(response)

# # Delete Respones
# response = requests.delete(BASE + "form/" + str(id_forms))
# print(response)

# =====================Test Panick route============================

# id_panick = 3
# data = {"id_users": 3,
#         "record_panick": "gs://sapaai-bucket/audio/test/test.flac",
#         "upload_date_panick": "dua hari lalu"}

# # # Post Respones
# response = requests.put(BASE + "panick/" + str(id_panick), data)
# print(response)

# # PAUSE
# input()

# # Get Respones
# response = requests.get(BASE + "panick/" + str(id_panick))
# print(response)

# # Delete Respones
# response = requests.delete(BASE + "panick/" + str(id_panick))
# print(response)
