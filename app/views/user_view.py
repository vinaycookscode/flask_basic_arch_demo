from flask import Blueprint, request, json
from flask.views import MethodView
from app.model.User import TblUser
from app import db
from app.serializers.user_serializer import UserSchema, UserModelSchema
from sqlalchemy.exc import DatabaseError
from marshmallow import ValidationError
from app.helpers.response import ApiResponse


user_blp = Blueprint('user_blp', __name__)


class UserView(MethodView):

    def get(self):

        return 'Hello Vinay'

    def post(self):

        final_data = []
        response_message = ''
        status = False
        http_code = 404
        errors = {}

        try:
            user_info = request.json.get('user_info', None)
            if user_info:
                user_schema = UserSchema()
                load_output = user_schema.load(user_info)

                if load_output.errors:
                    response_message = 'Data validation errors'
                    status = False
                    http_code = 400
                    errors = load_output.errors

                else:

                    user_record = TblUser(
                        first_name=user_info['first_name'],
                        mid_name=user_info['mid_name'],
                        surname=user_info['surname'],
                        birthday=user_info['birthday'],
                        mobile_no=user_info['mobile_no'],
                        linkedin_profile=user_info['linkedin_profile']
                    )
                    db.session.add(user_record)

                    if db.session.commit() is None:
                        user_model_schema_record = user_schema.dump(user_record)
                        status = True
                        http_code = 201
                        response_message = 'Data inserted'
                        print (user_model_schema_record)
                        final_data.append(user_model_schema_record.data)

                    else:
                        status = False
                        http_code = 400
                        response_message = 'Error while inserting a record'

        except ValidationError as ve:
            response_message = 'Required : ' + str(ve)
            print(json.dumps(ve))
            status = False
            http_code = 422
            final_data = []

        except DatabaseError as de:
            response_message = 'Exception ,' + str(de)
            print(response_message)
            status = False
            http_code = 400
            final_data = []

        except Exception as e:
            response_message = 'Exception ,' + str(e)
            print(response_message)
            status = False
            http_code = 400
            final_data = []
        finally:
            db.session.close()

        return ApiResponse.response(data=final_data, msg=response_message, status=status, http_code=http_code,
                                 errors=errors)

    def delete(self):
            pass


user_blp.add_url_rule('/users/', view_func=UserView.as_view('users'))
