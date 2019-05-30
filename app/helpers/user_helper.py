from app.model.User import TblUser
from app.serializers.user_serializer import UserSchema
from app import db
from app.helpers.response import ApiResponse


class UserHelper(object):
    user_schema = None

    def __init__(self):
        pass

    @staticmethod
    def insert(user_info):
        user_schema = UserSchema()
        final_data= []
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
            final_data.append(user_model_schema_record.data)
            return ApiResponse.functional_response(status=True, data=final_data)
        else:
            return ApiResponse.functional_response(status=False, data=final_data)