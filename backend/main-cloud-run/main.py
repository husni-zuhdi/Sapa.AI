#! /usr/bin/python3
# Import packages
import os
from flask import Flask
from flask_restful import Api, Resource, reqparse, fields, marshal_with
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
call = db.reference('call/')
process = db.reference('process/')
users = db.reference('users/')

# Form Arguments
form_get_args = reqparse.RequestParser()
form_get_args.add_argument("id_forms", type=str, help="Forms ID is required", required=True)

form_post_args = reqparse.RequestParser()
form_post_args.add_argument("id_users", type=str, help="Users ID is required", required=True)
form_post_args.add_argument("nama_korban_forms", type=str, help="Victim name is required", required=True)
form_post_args.add_argument("nama_tersangka_forms", type=str, help="Suspect name is required", required=True)
form_post_args.add_argument("kronologi_forms", type=str, help="Description is required", required=True)
form_post_args.add_argument("flag_layanan1", type=bool, help="Service 1")
form_post_args.add_argument("flag_layanan2", type=bool, help="Service 2")
form_post_args.add_argument("flag_layanan3", type=bool, help="Service 3")
form_post_args.add_argument("flag_layanan4", type=bool, help="Service 4")
form_post_args.add_argument("flag_layanan5", type=bool, help="Service 5")
form_post_args.add_argument("flag_layanan6", type=bool, help="Service 6")
form_post_args.add_argument("flag_layanan7", type=bool, help="Service 7")
form_post_args.add_argument("flag_layanan8", type=bool, help="Service 8")
form_post_args.add_argument("foto_forms", type=str, help="Photos")
form_post_args.add_argument("lokasi_forms", type=str, help="Location is required", required=True)
form_post_args.add_argument("upload_date_forms", type=str, help="Upload time is required", required=True)

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

forms_post_resource_fields = {
    'id_forms': fields.String,
    }

# From Service
class Forms_get(Resource):
    """
    Build Form API to
    1. GET report from database
    """

    @marshal_with(form_get_resource_fields)
    def get(self):
        args = form_get_args.parse_args()
        down_forms_ref = db.reference('forms/' + str(args['id_forms']))
        down_forms = down_forms_ref.get()
        return down_forms, 200

# From Service
class Forms_post(Resource):
    """
    Build Form API to
    2. PUT report from end users
    """

    @marshal_with(forms_post_resource_fields)
    def post(self):
        args = form_post_args.parse_args()
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

# From Service
# class Forms_delete(Resource):
#     """
#     Build Form API to
#     3. DELETE report from database by end users
#     """
    
#     def delete(self, id_forms):
#         # Masih development
#         result = FormsModel.query.filter_by(id_forms=id_forms).first()
#         if not result:
#             abort(404, message=f"Could not find the report with ID: {id_forms}...")
#         forms = FormsModel.query.filter_by(id_forms=id_forms).delete()
#         db.session.add(forms)
#         db.session.commit()
#         return f"Form with ID: {id_forms} successfully deleted", 204

# call Arguments
call_get_args = reqparse.RequestParser()
call_get_args.add_argument("id_call", type=str, help="call ID is required", required=True)
call_get_args.add_argument("id_process", type=str, help="Process ID is required", required=True)

call_post_args = reqparse.RequestParser()
call_post_args.add_argument("id_users", type=str, help="Users ID is required", required=True)
call_post_args.add_argument("record_call", type=str, help="Record URI is required", required=True)
call_post_args.add_argument("upload_date_call", type=str, help="Upload time is required", required=True)

# call Resource Fields
call_resource_fields = {
    'id_call': fields.String,
    'id_process': fields.String,
    'upload_date_call': fields.String,
    'flag_layanan1': fields.Boolean,
    'flag_layanan2': fields.Boolean,
    'flag_layanan3': fields.Boolean,
    'flag_layanan4': fields.Boolean,
    'flag_layanan5': fields.Boolean,
    'flag_layanan6': fields.Boolean,
    'flag_layanan7': fields.Boolean,
    'flag_layanan8': fields.Boolean
    }

call_post_resource_fields = {
    'id_call': fields.String,
    'id_process': fields.String
    }

# From Service
class Call_get(Resource):
    """
    Build call API to
    1. GET report from database
    """

    @marshal_with(call_resource_fields)
    def get(self):
        args = call_get_args.parse_args()
        down_call_ref = db.reference('call/' + str(args['id_call']))
        down_process_ref = db.reference('process/' + str(args['id_process']))
        down_call = down_call_ref.get()
        down_process = down_process_ref.get()

        # Query Return
        send_data={"id_call":args['id_call'],
                    "id_process":args['id_process'],
                    "upload_date_call":down_call['upload_date_call'],
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

# From Service
class Call_post(Resource):
    """
    Build call API to
    2. PUT report from end users
    """

    @marshal_with(call_post_resource_fields)
    def post(self):
        args_call = call_post_args.parse_args()
        data = {"id_users":args_call['id_users'],
                "record_call":args_call['record_call'],
                "upload_date_call":args_call['upload_date_call']
        }
        up_call = call.push(data)
        id_call = up_call.key

        # Start Processing Recorded Voices
        text = transcribe_sound(args_call['record_call'])
        instances=[text]
        version="v3"
        pred_test = predict_json(instances, version)

        result = {
            "id_call":id_call,
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
        send_data={"id_call":id_call,
                    "id_process":id_process
                    }

        return send_data, 201

# # From Service
# class Call_delete(Resource):
#     """
#     Build call API to
#     3. DELETE report from database by end users
#     """

#     def delete(self, id_call):
#         # Masih development
#         result = FormsModel.query.filter_by(id_call=id_call).first()
#         if not result:
#             abort(404, message=f"Could not find the report with ID: {id_call}...")
#         forms = FormsModel.query.filter_by(id_call=id_call).delete()
#         db.session.add(forms)
#         db.session.commit()
#         return f"Form with ID: {id_call} successfully deleted", 204


class Home(Resource):
    def get(self):
        return "Welcome to Sapa.AI API! You can use our Foms Service or Call Service", 200

api.add_resource(Home, '/')
api.add_resource(Forms_get, '/forms/get')
api.add_resource(Forms_post, '/forms/post')
api.add_resource(Call_get, '/call/get')
api.add_resource(Call_post, '/call/post')

# Test Main
if __name__ == "__main__":
    # app.run(debug=True)
    app.run()

# # Deploy Main
# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
