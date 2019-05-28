from flask import Flask,Blueprint
from flask_sqlalchemy import SQLAlchemy
from app.config.db_constants import DB_LOCAL
from app.views.user_view import user_blp
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_LOCAL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)
app.register_blueprint(user_blp)

from app.model.User import TblUser

