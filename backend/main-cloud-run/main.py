# Import packages
import os
from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from google.auth.environment_vars import PROJECT
from flask_sqlalchemy import SQLAlchemy

# Import from py files
from stt import transcribe_sound
from ml import predict_json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mock-database/database.db'
api = Api(app)
db = SQLAlchemy(app)                                                            # wraping app with Mock SQL database

#Build Mock Databases
class UsersModel(db.Model):
    """
    Buil a mock SQL database for Users table
    """
    id_users = db.Column(db.Integer, primary_key=True, nullable=False)  # primary_key=True mean it's unique
    username_users = db.Column(db.String(10), nullable=False)           # nullable=False mean it should not empty
    full_name_users = db.Column(db.String(50), nullable=False)
    mail_users = db.Column(db.String(30), nullable=False)
    phone_users = db.Column(db.String(14), nullable=False)
    password_users = db.Column(db.String(30), nullable=False)
    avatar_users = db.Column(db.String(50), nullable=False)
    ttl_users = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return {"id_users":id_users,
                "username_users":username_users,
                "full_name_users":full_name_users,
                "mail_users":mail_users,
                "phone_users":phone_users,
                "password_users":password_users,
                "avatar_users":avatar_users,
                "ttl_users":ttl_users
        }

class FormsModel(db.Model):
    """
    Buil a mock SQL database for Forms table
    """
    id_forms = db.Column(db.Integer, primary_key=True, nullable=False)
    id_users = db.Column(db.Integer, nullable=False)
    nama_korban_forms = db.Column(db.String(50), nullable=False)
    nama_tersangka_forms = db.Column(db.String(50), nullable=False)
    kronologi_forms = db.Column(db.String(1000), nullable=False)
    flag_layanan1 = db.Column(db.Boolean)
    flag_layanan2 = db.Column(db.Boolean)
    flag_layanan3 = db.Column(db.Boolean)
    flag_layanan4 = db.Column(db.Boolean)
    flag_layanan5 = db.Column(db.Boolean)
    flag_layanan6 = db.Column(db.Boolean)
    flag_layanan7 = db.Column(db.Boolean)
    flag_layanan8 = db.Column(db.Boolean)
    foto_forms = db.Column(db.String(50))
    lokasi_forms = db.Column(db.String(100), nullable=False)
    upload_date_forms = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return {"id_forms":id_forms,
                "id_users":id_users,
                "nama_korban_forms":nama_korban_forms,
                "nama_tersangka_forms":nama_tersangka_forms,
                "kronologi_forms":kronologi_forms,
                "flag_layanan1":flag_layanan1,
                "flag_layanan2":flag_layanan2,
                "flag_layanan3":flag_layanan3,
                "flag_layanan4":flag_layanan4,
                "flag_layanan5":flag_layanan5,
                "flag_layanan6":flag_layanan6,
                "flag_layanan7":flag_layanan7,
                "flag_layanan8":flag_layanan8,
                "foto_forms":foto_forms,
                "lokasi_forms":lokasi_forms,
                "upload_date_forms":upload_date_forms
        }

class PanickModel(db.Model):
    """
    Buil a mock SQL database for Panick table
    """
    id_panick = db.Column(db.Integer, primary_key=True, nullable=False)
    id_users = db.Column(db.Integer, nullable=False)
    record_panick = db.Column(db.String(500), nullable=False)
    upload_date_panick = db.Column(db.Date, nullable=False)
    
    def __repr__(self):
        return {"id_panick":id_panick,
                "id_users":id_users,
                "record_panick":record_panick,
                "upload_date_panick":upload_date_panick
        }

class ProcessModel(db.Model):
    """
    Buil a mock SQL database for Process table
    """
    id_process = db.Column(db.Integer, primary_key=True, nullable=False)
    id_panick = db.Column(db.Integer, nullable=False)
    result_process = db.Column(db.String(500), nullable=False)
    flag_layanan1 = db.Column(db.Integer, nullable=False)
    flag_layanan2 = db.Column(db.Integer, nullable=False)
    flag_layanan3 = db.Column(db.Integer, nullable=False)
    flag_layanan4 = db.Column(db.Integer, nullable=False)
    flag_layanan5 = db.Column(db.Integer, nullable=False)
    flag_layanan6 = db.Column(db.Integer, nullable=False)
    flag_layanan7 = db.Column(db.Integer, nullable=False)
    flag_layanan8 = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return {"id_process":id_process,
                "id_panick":id_panick,
                "result_process":result_process,
                "flag_layanan1":flag_layanan1,
                "flag_layanan2":flag_layanan2,
                "flag_layanan3":flag_layanan3,
                "flag_layanan4":flag_layanan4,
                "flag_layanan5":flag_layanan5,
                "flag_layanan6":flag_layanan6,
                "flag_layanan7":flag_layanan7,
                "flag_layanan8":flag_layanan8
        }
#db.create_all() # Run it once

# Set cloud run backend service account key
os.environ['GOOGLE_APPLICATION_CREDENTIALS']="main_key.json"

# From Service Num 2
class From(Resource):
    """
    Build Form API to
    1. GET report from database
    2. PUT report from end users
    3. DELETE report from database by end users
    """

    # Put Arguments
    form_put_args = reqparse.RequestParser()
    form_put_args.add_argument("id_users", type=str, help="Users ID is required", required=True)
    form_put_args.add_argument("id_forms", type=int, help="Form ID is required", required=True)
    form_put_args.add_argument("nama_korban_forms", type=int, help="Victim name is required", required=True)
    form_put_args.add_argument("nama_tersangka_forms", type=int, help="Suspect name is required", required=True)
    form_put_args.add_argument("kronologi_forms", type=int, help="Description is required", required=True)
    form_put_args.add_argument("flag_layanan1", type=int, help="Service 1")
    form_put_args.add_argument("flag_layanan2", type=int, help="Service 2")
    form_put_args.add_argument("flag_layanan3", type=int, help="Service 3")
    form_put_args.add_argument("flag_layanan4", type=int, help="Service 4")
    form_put_args.add_argument("flag_layanan5", type=int, help="Service 5")
    form_put_args.add_argument("flag_layanan6", type=int, help="Service 6")
    form_put_args.add_argument("flag_layanan7", type=int, help="Service 7")
    form_put_args.add_argument("flag_layanan8", type=int, help="Service 8")
    form_put_args.add_argument("foto_forms", type=int, help="Photos")
    form_put_args.add_argument("lokasi_forms", type=int, help="Location is required", required=True)
    form_put_args.add_argument("upload_date_forms", type=int, help="Upload time is required", required=True)

    def get(self, id_users, id_forms):
        result = FormsModel.query.filter_by(id_users=id_users, id_forms=id_forms).first()
        if not result:
            abort(404, message=f"Could not find the report from {id_users} with {id_forms} ID...")
        return result

    def put(self, id_users):
        args = form_put_args.parse_args()
        # Query ke database buat dapat id_forms terbaru
        # Buat variabel untuk menampung nilai tersebut
        id_forms=100 # variabel id_forms
        result = FormsModel(id_users=id_users,
                            id_forms=id_forms,
                            name=args['name'],
                            views=args['views'],
                            likes=args['likes']
                            )
        db.session.add(video) # add video to db
        db.session.commit() # commit change to db
        return video, 201

api.add_resource(form, '/form')
api.add_resource(panick, '/panick')

# Test Main
if __name__ == "__main__":
    app.run(debug=True)

# # Form Service
# @app.route("/form", methods=['GET', 'POST', 'DELETE'])
# def form():
#     form = os.environ.get("NAME", "to Form")
#     return jsonify(form)
#
# # Panick Service
# @app.route("/panick", methods=['GET', 'POST', 'DELETE'])
# def panick():
#     # Text-to-speech
#     gcs_uri="gs://sapaai-bucket/audio/test/test.flac"
#     text = stt.transcribe_sound(gcs_uri)
#
#     # Variabel-variabel model
#     instances=[text['transcript']]
#     version="v0_2"
#
#     # Predict Solutions
#     predict = predict_json(instances, version)
#
#     return predict

# Deploy Main
# if __name__ == "__main__":
#     app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))