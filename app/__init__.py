from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from config.db_constants import DB_LOCAL
from flask_migrate import Migrate

sql_alchemy = SQLAlchemy()
migrate = Migrate()
#https://flask-migrate.readthedocs.io/en/latest/

def create_app():

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = DB_LOCAL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    init_packages(app)


def init_packages(app):
    marshmallow = Marshmallow()
    sql_alchemy.init_app(app)
    marshmallow.init_app(app)
    migrate = Migrate(app, sql_alchemy)
