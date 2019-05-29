from app import ma
from app.model.User import TblUser
from marshmallow import fields


class UserModelSchema(ma.ModelSchema):
    class Meta:
        model = TblUser


class UserSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    first_name = fields.Str(required=True)
    mid_name = fields.Str(required=True)
    surname = fields.Str(required=True)
    birthday = fields.Date(required=True)
    mobile_no = fields.Str(required=True)
    linkedin_profile = fields.Str(required=False)
