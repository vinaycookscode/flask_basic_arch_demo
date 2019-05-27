from flask import Blueprint
from flask.views import MethodView
from app import app
user_blp = Blueprint('user_blp')


class UserView(MethodView):
    def get(self):
        pass

    def post(self):
        pass

    def delete(self):
        pass

app.add_url_rule('/users/', view_func=UserView.as_view('users'))
