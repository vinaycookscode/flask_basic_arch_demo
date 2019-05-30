from flask import Blueprint, request, json
from flask.views import MethodView
from app.model.User import TblUser
from app import db
from app.serializers.user_serializer import UserSchema, UserModelSchema
from sqlalchemy.exc import DatabaseError
from marshmallow import ValidationError
from app.helpers.response import ApiResponse
from app.req_validation.user_data_validation import UserDataValid
from app.config.static_messages import StaticMessage
from app.helpers.user_helper import UserHelper
user_blp = Blueprint('user_blp', __name__)


@user_blp.before_request
def before_req():

    if request.method == 'POST':
        user_info = request.json.get('user_info', None)
        validation_resp = UserDataValid.load_user_data(user_data=user_info)

        if validation_resp['status'] is not True:

            return ApiResponse.response(data=[], msg=validation_resp['response_message'],
                                        status=validation_resp['status'],
                                        http_code=validation_resp['http_code'],
                                        errors=validation_resp['errors'])


class UserView(MethodView):

    def get(self):

        return 'Hello Vinay'

    @staticmethod
    def post():

        final_data = []
        response_message = ''
        status = False
        http_code = 404
        errors = {}

        try:
            static_message = StaticMessage()
            user_info = request.json.get('user_info', None)
            if user_info:
                helper_response = UserHelper.insert(user_info=user_info)
                if helper_response['status']:
                    user_model_schema_record = helper_response['data']
                    status = True
                    http_code = 201
                    response_message = static_message.DATA_INSERTED
                    final_data = user_model_schema_record

                else:
                    status = False
                    http_code = 400
                    response_message = StaticMessage.ERROR_WHILE_INSERTING

        except ValidationError as ve:
            response_message = 'Required : ' + str(ve)
            print(json.dumps(ve))
            status = False
            http_code = 422
            final_data = []

        except DatabaseError as de:
            response_message = 'Exception1 ,' + str(de)
            print(response_message)
            status = False
            http_code = 400
            final_data = []

        except Exception as e:
            response_message = 'Exception2 ,' + str(e)
            print(response_message)
            status = False
            http_code = 400
            final_data = []
            db.session.rollback()

        finally:
            db.session.close()

        return ApiResponse.response(data=final_data, msg=response_message, status=status, http_code=http_code,
                                 errors=errors)

    def delete(self):
            pass


user_blp.add_url_rule('/users/', view_func=UserView.as_view('users'))
