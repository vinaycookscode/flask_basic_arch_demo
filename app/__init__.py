from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


def create_app():

    app = Flask(__name__)
    init_packages(app)


def init_packages(app):
    sql_alchemy = SQLAlchemy()
    marshmallow = Marshmallow()
    sql_alchemy.init_app(app)
    marshmallow.init_app(app)
