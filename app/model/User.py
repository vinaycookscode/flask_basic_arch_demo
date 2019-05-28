from sqlalchemy import Column, Integer, String, ForeignKey, Date
from app import db


class TblUser(db.Model):

    __tablename__ = 'tbl_user'

    id = db.Column(Integer, primary_key=True)
    first_name = db.Column(String(100), unique=False, nullable=True)
    mid_name = db.Column(String(100), default=' ')
    surname = db.Column(String(100), default='')
    birthday = db.Column(Date, nullable=True, default='')
    mobile_no = db.Column(String(10))
    linkedin_profile = db.Column(String(100), nullable=True, )

    def __repr__(self):

        return self.first_name
