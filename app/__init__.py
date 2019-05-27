from flask import Flask,Blueprint
from flask_sqlalchemy import SQLAlchemy
from config.db_constants import DB_LOCAL
from app.views.user_view import user_blp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_LOCAL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.regisetr_blueprint(user_blp)

from model.User import TblUser

