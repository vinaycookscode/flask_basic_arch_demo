from app import ma
from app.model.User import TblUser
from flask_marshmallow import fields


class UserModelSchema(ma.ModelSchema):
    class Meta:
        model = TblUser


class UserSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    surname = fields.String(required=True)
    birthday = fields.DateTime(required=True)
    mobile_no = fields.String(required=True)
    linkedin_profile = fields.String(required=False)
