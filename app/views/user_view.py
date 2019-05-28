from flask import Blueprint, request, json
from flask.views import MethodView
from app.model.User import TblUser
from app.serializers.user_serializer import UserSchema
from werkzeug.exceptions import NotFound
from sqlalchemy.exc import DatabaseError
from marshmallow import ValidationError

user_blp = Blueprint('user_blp', __name__)


class UserView(MethodView):

    def get(self):

        return 'Hello Vinay'

    def post(self):

        venue_sub_input_data = {}
        response_message = ''
        status = False
        http_code = 404
        errors = {}

        try:
            user_info = request.json.get('user_info', None)
            if user_info:
                user_schema = UserSchema()
                load_output = user_schema.load(venue_sub_input_data)

                if load_output.errors:
                    response_message = 'Data validation errors'
                    status = False
                    http_code = 400
                    errors = load_output.errors

                else:

                    user_record = TblUser(
                        first_name=user_info.first_name,
                        midname=user_info.mid_name,
                        surname=user_info.surname,
                        birthday=user_info.birthday,

                    )



        except ValidationError as ve:
            response_message = 'Required : ' + str(ve)
            print(json.dumps(ve))
            status = False
            http_code = 422
            venue_sub_input_data = []

        except DatabaseError as de:
            response_message = 'Exception ,' + str(de)
            print(response_message)
            status = False
            http_code = 400
            venue_sub_input_data = []

        except Exception as e:
            response_message = 'Exception ,' + str(e)
            print(response_message)
            status = False
            http_code = 400
            venue_sub_input_data = []


def delete(self):
        pass


user_blp.add_url_rule('/users/', view_func=UserView.as_view('users'))
