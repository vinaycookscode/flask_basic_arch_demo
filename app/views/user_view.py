from flask import Blueprint, request, json
from flask.views import MethodView
from app import db
from sqlalchemy.exc import DatabaseError
from marshmallow import ValidationError
from app.helpers.response import ApiResponse
from app.req_validation.user_data_validation import UserDataValid
from app.config.static_messages import StaticMessage
from app.helpers.user_helper import UserHelper
from app.serializers.user_serializer import UserModelSchema,UserSchema

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

    def get(self, id):
        final_data = []
        response_message = ''
        status = False
        http_code = 404
        errors = {}
        try:
            user_info = UserHelper.get() if not id else UserHelper.get(user_id=id)

            if user_info:
                user_model_schema = UserModelSchema(many=True)
                final_user_info = user_model_schema.dump(user_info)
                final_data = final_user_info.data
                if len(final_data) > 0:
                    status = True
                    http_code = 200
                    errors = {}
                else:
                    status = False
                    http_code = 400
                    errors = {}

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

        return ApiResponse.response(data=final_data, msg=response_message, status=status, http_code=http_code,
                                    errors=errors)

    @staticmethod
    def post(id):

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

    def delete(self, id):

        final_data = []
        response_message = ''
        status = False
        http_code = 404
        errors = {}
        try:
            user_info = UserHelper.get(user_id=id)
            if user_info:
                is_user_updated = UserHelper.deactivate_user(user_data=user_info[0], is_active=False)
                if is_user_updated:
                    status = True
                    http_code = 201
                    errors = {}
                    response_message = StaticMessage.USER_DEACTIVATED
                else:
                    status = False
                    http_code = 400
                    errors = {}
                    response_message = StaticMessage.ERROR_WHILE_DEACTIVATING
            else:
                response_message = StaticMessage.NO_DATA_FOUND

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

        return ApiResponse.response(data=final_data, msg=response_message, status=status, http_code=http_code,
                                    errors=errors)

    def put(self, id):
        final_data = []
        response_message = ''
        status = False
        http_code = 404
        errors = {}
        try:
            user_info_json = request.json.get('user_info', None)
            if user_info_json:
                is_user_updated = UserHelper.update_user(id=user_info_json['id'], new_user_data=user_info_json)
                if is_user_updated:
                    status = True
                    http_code = 201
                    errors = {}
                    response_message = StaticMessage.DATA_UPDATED
                else:
                    status = False
                    http_code = 400
                    errors = {}
                    response_message = StaticMessage.ERROR_WHILE_UPDATING
            else:
                response_message = StaticMessage.NO_DATA_FOUND

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


user_blp.add_url_rule('/users/', defaults={'id': None},  view_func=UserView.as_view('users'), methods=['GET','POST','PUT'])
user_blp.add_url_rule('/users/<int:id>/', view_func=UserView.as_view('users_by_id'), methods=['GET','DELETE'])
