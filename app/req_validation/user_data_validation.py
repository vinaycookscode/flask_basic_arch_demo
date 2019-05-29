from app.serializers.user_serializer import UserSchema


class UserDataValid(object):
    def __init__(self):
        pass

    @staticmethod
    def load_user_data(user_data):
        user_schema = UserSchema()
        load_output = user_schema.load(user_data)

        if load_output.errors:
            return {
                'response_message': 'Data validation errors',
                'status': False,
                'http_code': 400,
                'errors': load_output.errors,
            }
        else:
            return {
                'response_message': 'Data validated',
                'status': True,
                'http_code': 200,
                'errors': 'No errors found',
            }
