from app.model.User import TblUser
from app.serializers.user_serializer import UserSchema
from app import db
from app.helpers.response import ApiResponse
from sqlalchemy import and_


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

    @staticmethod
    def get(user_id=None, linkedin_profile=None):
        user_info = None

        if user_id and linkedin_profile :
            user_info = TblUser.query.filter(and_(TblUser.id == user_id,
                                                  TblUser.linkedin_profile == linkedin_profile
                                                  )
                                             ).all()
        elif user_id:
            user_info = TblUser.query.filter(TblUser.id == user_id).all()

        elif linkedin_profile:
            user_info = TblUser.query.filter(TblUser.id == user_id).all()

        else:
            user_info = TblUser.query.all()

        return user_info

    @staticmethod
    def deactivate_user(user_data, is_active=False):
        user_data.is_active = is_active
        if db.session.merge(user_data):
            return True
        else:
            return False

    @staticmethod
    def update_user(id, new_user_data):
        old_user_data = UserHelper.get(user_id=id)
        old_user_data = old_user_data[0]

        old_user_data.first_name = new_user_data['first_name']
        old_user_data.mid_name = new_user_data['mid_name']
        old_user_data.surname = new_user_data['surname']
        old_user_data.birthday = new_user_data['birthday']
        old_user_data.mobile_no = new_user_data['mobile_no']
        old_user_data.linkedin_profile = new_user_data['linkedin_profile']
        old_user_data.is_active = new_user_data['is_active']

        db.session.merge(old_user_data)

        if db.session.commit() is None:
            return True
        else:
            return False
