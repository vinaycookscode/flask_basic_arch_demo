from flask import Flask,Blueprint
from flask_sqlalchemy import SQLAlchemy
from app.config.db_constants import DB_LOCAL

from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_LOCAL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy()
db.init_app(app)
ma = Marshmallow()
ma.init_app(app)

from app.views.user_view import user_blp
app.register_blueprint(user_blp)
from app.model.User import TblUser

