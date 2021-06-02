# Import packages
from datetime import datetime
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

# Set cloud run backend service account key
os.environ['GOOGLE_APPLICATION_CREDENTIALS']="main_key.json"

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
    upload_date_forms = db.Column(db.String(100), nullable=False)

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
# db.create_all() # Run it once

# Form Put Arguments
form_put_args = reqparse.RequestParser()
form_put_args.add_argument("id_users", type=int, help="Users ID is required", required=True)
form_put_args.add_argument("nama_korban_forms", type=str, help="Victim name is required", required=True)
form_put_args.add_argument("nama_tersangka_forms", type=str, help="Suspect name is required", required=True)
form_put_args.add_argument("kronologi_forms", type=str, help="Description is required", required=True)
form_put_args.add_argument("flag_layanan1", type=bool, help="Service 1")
form_put_args.add_argument("flag_layanan2", type=bool, help="Service 2")
form_put_args.add_argument("flag_layanan3", type=bool, help="Service 3")
form_put_args.add_argument("flag_layanan4", type=bool, help="Service 4")
form_put_args.add_argument("flag_layanan5", type=bool, help="Service 5")
form_put_args.add_argument("flag_layanan6", type=bool, help="Service 6")
form_put_args.add_argument("flag_layanan7", type=bool, help="Service 7")
form_put_args.add_argument("flag_layanan8", type=bool, help="Service 8")
form_put_args.add_argument("foto_forms", type=str, help="Photos")
form_put_args.add_argument("lokasi_forms", type=str, help="Location is required", required=True)
form_put_args.add_argument("upload_date_forms", type=str, help="Upload time is required", required=True)

# Form Resource Fields
form_resource_fields = {
    'id_forms': fields.Integer,
    'id_users': fields.Integer,
    'nama_korban_forms': fields.String,
    'nama_tersangka_forms': fields.String,
    'kronologi_forms': fields.String,
    'flag_layanan1': fields.Boolean,
    'flag_layanan2': fields.Boolean,
    'flag_layanan3': fields.Boolean,
    'flag_layanan4': fields.Boolean,
    'flag_layanan5': fields.Boolean,
    'flag_layanan6': fields.Boolean,
    'flag_layanan7': fields.Boolean,
    'flag_layanan8': fields.Boolean,
    'foto_forms': fields.String,
    'lokasi_forms': fields.String,
    'upload_date_forms': fields.String
    }

# From Service
class Form(Resource):
    """
    Build Form API to
    1. GET report from database
    2. PUT report from end users
    3. DELETE report from database by end users
    """

    @marshal_with(form_resource_fields)
    def get(self, id_forms):
        result = FormsModel.query.filter_by(id_forms=id_forms).first()
        if not result:
            abort(404, message=f"Could not find the report with ID: {id_forms}...")
        return result

    @marshal_with(form_resource_fields)
    def put(self, id_forms):
        args = form_put_args.parse_args()
        # Query ke database buat dapat id_forms terbaru atau
        # dari android Query terlebih dahulu ke Realtime Database dan passing id_forms sama argumen2 lainnya
        result = FormsModel.query.filter_by(id_forms=id_forms).first()
        if result:
            abort(409, message=f"Report ID: {id_forms} already taken...")
        forms = FormsModel(id_forms=id_forms,
                            id_users=args['id_users'],
                            nama_korban_forms=args['nama_korban_forms'],
                            nama_tersangka_forms=args['nama_tersangka_forms'],
                            kronologi_forms=args['kronologi_forms'],
                            flag_layanan1=args['flag_layanan1'],
                            flag_layanan2=args['flag_layanan2'],
                            flag_layanan3=args['flag_layanan3'],
                            flag_layanan4=args['flag_layanan4'],
                            flag_layanan5=args['flag_layanan5'],
                            flag_layanan6=args['flag_layanan6'],
                            flag_layanan7=args['flag_layanan7'],
                            flag_layanan8=args['flag_layanan8'],
                            foto_forms=args['foto_forms'],
                            lokasi_forms=args['lokasi_forms'],
                            upload_date_forms=args['upload_date_forms']
                            )
        db.session.add(forms)                                               # Add forms to Form Database
        db.session.commit()                                                 # Commit change to Form Database
        return forms, 201

    @marshal_with(form_resource_fields)
    def delete(self, id_forms):
        # Masih development
        result = FormsModel.query.filter_by(id_forms=id_forms).first()
        if not result:
            abort(404, message=f"Could not find the report with ID: {id_forms}...")
        forms = FormsModel.query.filter_by(id_forms=id_forms).delete()
        db.session.add(forms)
        db.session.commit()
        return f"Form with ID: {id_forms} successfully deleted", 204

# class PanickModel(db.Model):
#     """
#     Buil a mock SQL database for Panick table
#     """
#     id_panick = db.Column(db.Integer, primary_key=True, nullable=False)
#     id_users = db.Column(db.Integer, nullable=False)
#     record_panick = db.Column(db.String(500), nullable=False)
#     upload_date_panick = db.Column(db.Date, nullable=False)
    
#     def __repr__(self):
#         return {"id_panick":id_panick,
#                 "id_users":id_users,
#                 "record_panick":record_panick,
#                 "upload_date_panick":upload_date_panick
#         }

# class ProcessModel(db.Model):
#     """
#     Buil a mock SQL database for Process table
#     """
#     id_process = db.Column(db.Integer, primary_key=True, nullable=False)
#     id_panick = db.Column(db.Integer, nullable=False)
#     result_process = db.Column(db.String(500), nullable=False)
#     flag_layanan1 = db.Column(db.Integer, nullable=False)
#     flag_layanan2 = db.Column(db.Integer, nullable=False)
#     flag_layanan3 = db.Column(db.Integer, nullable=False)
#     flag_layanan4 = db.Column(db.Integer, nullable=False)
#     flag_layanan5 = db.Column(db.Integer, nullable=False)
#     flag_layanan6 = db.Column(db.Integer, nullable=False)
#     flag_layanan7 = db.Column(db.Integer, nullable=False)
#     flag_layanan8 = db.Column(db.Integer, nullable=False)
    
#     def __repr__(self):
#         return {"id_process":id_process,
#                 "id_panick":id_panick,
#                 "result_process":result_process,
#                 "flag_layanan1":flag_layanan1,
#                 "flag_layanan2":flag_layanan2,
#                 "flag_layanan3":flag_layanan3,
#                 "flag_layanan4":flag_layanan4,
#                 "flag_layanan5":flag_layanan5,
#                 "flag_layanan6":flag_layanan6,
#                 "flag_layanan7":flag_layanan7,
#                 "flag_layanan8":flag_layanan8
#         }

# Panick Put Arguments
panick_put_args = reqparse.RequestParser()
panick_put_args.add_argument("id_users", type=int, help="Users ID is required", required=True)
panick_put_args.add_argument("record_panick", type=str, help="Record URI is required", required=True)
panick_put_args.add_argument("upload_date_panick", type=str, help="Upload time is required", required=True)

# Panick Resource Fields
panick_resource_fields = {
    'id_forms': fields.Integer,
    'id_users': fields.Integer,
    'nama_korban_forms': fields.String,
    'nama_tersangka_forms': fields.String,
    'kronologi_forms': fields.String,
    'flag_layanan1': fields.Boolean,
    'flag_layanan2': fields.Boolean,
    'flag_layanan3': fields.Boolean,
    'flag_layanan4': fields.Boolean,
    'flag_layanan5': fields.Boolean,
    'flag_layanan6': fields.Boolean,
    'flag_layanan7': fields.Boolean,
    'flag_layanan8': fields.Boolean,
    'foto_forms': fields.String,
    'lokasi_forms': fields.String,
    'upload_date_forms': fields.String
    }


# From Service
class Panick(Resource):
    """
    Build Panick API to
    1. GET report from database
    2. PUT report from end users
    3. DELETE report from database by end users
    """

    @marshal_with(panick_resource_fields)
    def get(self, id_panick):
        result = FormsModel.query.filter_by(id_panick=id_panick).first()
        if not result:
            abort(404, message=f"Could not find the report with ID: {id_panick}...")
        return result

    @marshal_with(panick_resource_fields)
    def put(self, id_panick):
        args = form_put_args.parse_args()
        # Query ke database buat dapat id_panick terbaru atau
        # dari android Query terlebih dahulu ke Realtime Database dan passing id_panick sama argumen2 lainnya
        result = FormsModel.query.filter_by(id_panick=id_panick).first()
        if result:
            abort(409, message=f"Report ID: {id_panick} already taken...")
        forms = FormsModel(id_panick=id_panick,
                            id_users=args['id_users'],
                            nama_korban_forms=args['nama_korban_forms'],
                            nama_tersangka_forms=args['nama_tersangka_forms'],
                            kronologi_forms=args['kronologi_forms'],
                            flag_layanan1=args['flag_layanan1'],
                            flag_layanan2=args['flag_layanan2'],
                            flag_layanan3=args['flag_layanan3'],
                            flag_layanan4=args['flag_layanan4'],
                            flag_layanan5=args['flag_layanan5'],
                            flag_layanan6=args['flag_layanan6'],
                            flag_layanan7=args['flag_layanan7'],
                            flag_layanan8=args['flag_layanan8'],
                            foto_forms=args['foto_forms'],
                            lokasi_forms=args['lokasi_forms'],
                            upload_date_forms=args['upload_date_forms']
                            )
        db.session.add(forms)
        db.session.commit()
        return forms, 201

    @marshal_with(panick_resource_fields)
    def delete(self, id_panick):
        # Masih development
        result = FormsModel.query.filter_by(id_panick=id_panick).first()
        if not result:
            abort(404, message=f"Could not find the report with ID: {id_panick}...")
        forms = FormsModel.query.filter_by(id_panick=id_panick).delete()
        db.session.add(forms)
        db.session.commit()
        return f"Form with ID: {id_panick} successfully deleted", 204

api.add_resource(Form, '/form<int:id_forms>')
api.add_resource(Panick, '/panick<int:id_panick>')

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