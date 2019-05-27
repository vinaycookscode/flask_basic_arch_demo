from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from flask_appbuilder import Model
from app import db
from flask_script import Manager


class TblUser(db.Model):
    id = db.Column(Integer, primary_key=True)
    first_name = db.Column(String(100), unique=False, nullable=True)
    last_name = db.Column(String(100), default='Street ')
    surname = db.Column(String(100), default='Street ')
    birthday = db.Column(Date)
    mobile_no = db.Column(String(10))
    linkedin_profile = db.Column(String(100), nullable=True, )

    def __repr__(self):

        return self.first_name
