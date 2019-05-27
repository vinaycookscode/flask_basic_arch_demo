# from flask import Flask, Blueprint
# from flask_sqlalchemy import SQLAlchemy
# from flask_marshmallow import Marshmallow
# from config.db_constants import DB_LOCAL
# from flask_migrate import Migrate
#
# #https://flask-migrate.readthedocs.io/en/latest/
#
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = DB_LOCAL
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
# db = SQLAlchemy()
# marshmallow = Marshmallow()
# db.init_app(app)
# marshmallow.init_app(app)
# migrate = Migrate(app, db)

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from config.db_constants import DB_LOCAL



app = Flask(__name__)
#app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_DATABASE_URI'] = DB_LOCAL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from model.User import TblUser

