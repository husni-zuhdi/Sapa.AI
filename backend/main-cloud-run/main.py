#! /usr/bin/python3
# Import packages
import os
from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from google.auth.environment_vars import PROJECT
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Import from py files
from stt import transcribe_sound
from ml import predict_json

app = Flask(__name__)
api = Api(app)

# Set cloud run backend service account key
os.environ['GOOGLE_APPLICATION_CREDENTIALS']="key.json"

# Fetch the service account key JSON file contents
cred = credentials.Certificate('key.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://sapaai-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

# Set firebase RDb references
forms = db.reference('forms/')
panick = db.reference('panick/')
process = db.reference('process/')
users = db.reference('users/')

# Form Arguments
form_get_args = reqparse.RequestParser()
form_get_args.add_argument("id_forms", type=str, help="Forms ID is required", required=True)

form_put_args = reqparse.RequestParser()
form_put_args.add_argument("id_users", type=str, help="Users ID is required", required=True)
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
form_get_resource_fields = {
    'id_users': fields.String,
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

forms_put_resource_fields = {
    'id_forms': fields.String,
    }

# From Service
class Form(Resource):
    """
    Build Form API to
    1. GET report from database
    2. PUT report from end users
    3. DELETE report from database by end users
    """

    # @marshal_with(form_get_resource_fields)
    def get(self):
        args = form_get_args.parse_args()
        down_forms_ref = db.reference('forms/' + str(args['id_forms']))
        down_forms = down_forms_ref.get()
        return down_forms, 200

    @marshal_with(forms_put_resource_fields)
    def put(self):
        args = form_put_args.parse_args()
        data = {"id_users":args['id_users'],
                "nama_korban_forms":args['nama_korban_forms'],
                "nama_tersangka_forms":args['nama_tersangka_forms'],
                "kronologi_forms":args['kronologi_forms'],
                "flag_layanan1":args['flag_layanan1'],
                "flag_layanan2":args['flag_layanan2'],
                "flag_layanan3":args['flag_layanan3'],
                "flag_layanan4":args['flag_layanan4'],
                "flag_layanan5":args['flag_layanan5'],
                "flag_layanan6":args['flag_layanan6'],
                "flag_layanan7":args['flag_layanan7'],
                "flag_layanan8":args['flag_layanan8'],
                "foto_forms":args['foto_forms'],
                "lokasi_forms":args['lokasi_forms'],
                "upload_date_forms":args['upload_date_forms']
                }
        up_forms = forms.push(data)
        id_forms = {"id_forms": up_forms.key}
        return id_forms, 201
    
    # def delete(self, id_forms):
    #     # Masih development
    #     result = FormsModel.query.filter_by(id_forms=id_forms).first()
    #     if not result:
    #         abort(404, message=f"Could not find the report with ID: {id_forms}...")
    #     forms = FormsModel.query.filter_by(id_forms=id_forms).delete()
    #     db.session.add(forms)
    #     db.session.commit()
    #     return f"Form with ID: {id_forms} successfully deleted", 204

# Panick Arguments
panick_get_args = reqparse.RequestParser()
panick_get_args.add_argument("id_panick", type=str, help="Panick ID is required", required=True)
panick_get_args.add_argument("id_process", type=str, help="Process ID is required", required=True)

panick_put_args = reqparse.RequestParser()
panick_put_args.add_argument("id_users", type=str, help="Users ID is required", required=True)
panick_put_args.add_argument("record_panick", type=str, help="Record URI is required", required=True)
panick_put_args.add_argument("upload_date_panick", type=str, help="Upload time is required", required=True)

# Panick Resource Fields
panick_resource_fields = {
    'id_panick': fields.String,
    'id_process': fields.String,
    'upload_date_panick': fields.String,
    'flag_layanan1': fields.Boolean,
    'flag_layanan2': fields.Boolean,
    'flag_layanan3': fields.Boolean,
    'flag_layanan4': fields.Boolean,
    'flag_layanan5': fields.Boolean,
    'flag_layanan6': fields.Boolean,
    'flag_layanan7': fields.Boolean,
    'flag_layanan8': fields.Boolean
    }

panick_put_resource_fields = {
    'id_panick': fields.String,
    'id_process': fields.String
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
    def get(self):
        args = panick_get_args.parse_args()
        down_panick_ref = db.reference('panick/' + str(args['id_panick']))
        down_process_ref = db.reference('process/' + str(args['id_process']))
        down_panick = down_panick_ref.get()
        down_process = down_process_ref.get()

        # Query Return
        send_data={"id_panick":args['id_panick'],
                    "id_process":args['id_process'],
                    "upload_date_panick":down_panick['upload_date_panick'],
                    "flag_layanan1":down_process['flag_layanan1'],
                    "flag_layanan2":down_process['flag_layanan2'],
                    "flag_layanan3":down_process['flag_layanan3'],
                    "flag_layanan4":down_process['flag_layanan4'],
                    "flag_layanan5":down_process['flag_layanan5'],
                    "flag_layanan6":down_process['flag_layanan6'],
                    "flag_layanan7":down_process['flag_layanan7'],
                    "flag_layanan8":down_process['flag_layanan8']
                    }
        return send_data, 200

    @marshal_with(panick_put_resource_fields)
    def put(self):
        args_panick = panick_put_args.parse_args()
        data = {"id_users":args_panick['id_users'],
                "record_panick":args_panick['record_panick'],
                "upload_date_panick":args_panick['upload_date_panick']
        }
        up_panick = panick.push(data)
        id_panick = up_panick.key

        # Start Processing Recorded Voices
        text = transcribe_sound(args_panick['record_panick'])
        instances=[text['transcript']]
        version="v3"
        pred_test = predict_json(instances, version)

        result = {
            "id_panick":id_panick,
            "result_process":instances[0],
            "flag_layanan1":pred_test[0][0],
            "flag_layanan2":pred_test[0][1],
            "flag_layanan3":pred_test[0][2],
            "flag_layanan4":pred_test[0][3],
            "flag_layanan5":pred_test[0][4],
            "flag_layanan6":pred_test[0][5],
            "flag_layanan7":pred_test[0][6],
            "flag_layanan8":pred_test[0][7]
        }
        up_process = process.push(result)
        id_process = up_process.key
        
        
        # Query Return
        send_data={"id_panick":id_panick,
                    "id_process":id_process
                    }

        return send_data, 201

    # def delete(self, id_panick):
    #     # Masih development
    #     result = FormsModel.query.filter_by(id_panick=id_panick).first()
    #     if not result:
    #         abort(404, message=f"Could not find the report with ID: {id_panick}...")
    #     forms = FormsModel.query.filter_by(id_panick=id_panick).delete()
    #     db.session.add(forms)
    #     db.session.commit()
    #     return f"Form with ID: {id_panick} successfully deleted", 204

class Home(Resource):
    def get(self):
        return "Welcome to Sapa.AI API!\nYou can use our Foms Service or Panick Service", 200

api.add_resource(Home, '/')
api.add_resource(Form, '/forms')
api.add_resource(Panick, '/panick')

# Test Main
if __name__ == "__main__":
    app.run()

# # Deploy Main
# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
