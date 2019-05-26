from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from flask_appbuilder import Model
from app import sql_alchemy
from flask_script import Manager

class TblUser(sql_alchemy.Model):
    id = sql_alchemy.Column(Integer, primary_key=True)
    first_name = sql_alchemy.Column(String(100), unique=False, nullable=True)
    last_name = sql_alchemy.Column(String(100), default='Street ')
    surname = sql_alchemy.Column(String(100), default='Street ')
    birthday = sql_alchemy.Column(Date)
    mobile_no = sql_alchemy.Column(String(10))
    linkedin_profile = sql_alchemy.Column(String(100), nullable=True, )

    def __repr__(self):
        return self.name